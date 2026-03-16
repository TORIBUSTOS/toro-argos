from __future__ import annotations

import os
import time
import asyncio
from dataclasses import dataclass
from typing import Any, Dict, Optional

import httpx
import pandas as pd


class FinnhubError(RuntimeError):
    pass


class FinnhubNoDataError(FinnhubError):
    pass


class FinnhubConfigError(FinnhubError):
    pass


@dataclass(frozen=True)
class CacheItem:
    expires_at: float
    value: Any


class _TinyTTLCache:
    def __init__(self):
        self._store: Dict[Any, CacheItem] = {}

    def get(self, key: Any) -> Optional[Any]:
        item = self._store.get(key)
        if not item:
            return None
        if time.time() >= item.expires_at:
            self._store.pop(key, None)
            return None
        return item.value

    def set(self, key: Any, value: Any, ttl_seconds: int) -> None:
        self._store[key] = CacheItem(expires_at=time.time() + ttl_seconds, value=value)


def _get_api_key(explicit: Optional[str] = None) -> Optional[str]:
    """
    Resolve FINNHUB key from:
    1) explicit argument
    2) app.core.settings (if exists)
    3) env FINNHUB_API_KEY / FINNHUB_TOKEN
    """
    if explicit:
        return explicit

    # Optional: use project settings if present (FastAPI common pattern)
    try:
        from app.core.settings import settings  # type: ignore
        key = getattr(settings, "FINNHUB_API_KEY", None)
        if key:
            return key
    except Exception:
        pass

    return os.getenv("FINNHUB_API_KEY") or os.getenv("FINNHUB_TOKEN")


class FinnhubClient:
    BASE_URL = "https://finnhub.io/api/v1"

    def __init__(self, api_key: Optional[str] = None, timeout: float = 10.0):
        self.api_key = _get_api_key(api_key)
        if not self.api_key:
            raise FinnhubConfigError("Missing FINNHUB_API_KEY (or FINNHUB_TOKEN) in env/settings.")

        self._timeout = timeout
        self._quote_cache = _TinyTTLCache()
        self._candles_cache = _TinyTTLCache()

        self._client = httpx.AsyncClient(
            base_url=self.BASE_URL,
            timeout=self._timeout,
            headers={"Accept": "application/json"},
        )

    async def aclose(self) -> None:
        await self._client.aclose()

    async def _request_json(self, path: str, params: Dict[str, Any]) -> Dict[str, Any]:
        params = dict(params)
        params["token"] = self.api_key

        last_exc: Optional[Exception] = None
        for attempt in range(3):  # 1 + 2 retries
            try:
                resp = await self._client.get(path, params=params)

                if resp.status_code in (429, 502, 503, 504):
                    await asyncio.sleep(0.4 * (2 ** attempt))
                    continue

                resp.raise_for_status()
                return resp.json()

            except (httpx.TimeoutException, httpx.NetworkError, httpx.HTTPStatusError) as e:
                last_exc = e
                if attempt == 2:
                    break
                await asyncio.sleep(0.4 * (2 ** attempt))

        raise FinnhubError(f"Finnhub request failed after retries: {last_exc}") from last_exc

    async def get_quote(self, symbol: str) -> Dict[str, Any]:
        """
        Finnhub endpoint: /quote

        Output keys (normalized):
          price, change, change_pct, high, low, open, prev_close, timestamp
        """
        symbol = symbol.strip().upper()
        cache_key = ("quote", symbol)
        cached = self._quote_cache.get(cache_key)
        if cached is not None:
            return cached

        data = await self._request_json("/quote", {"symbol": symbol})

        try:
            normalized = {
                "price": float(data.get("c", 0.0)),
                "change": float(data.get("d", 0.0)),
                "change_pct": float(data.get("dp", 0.0)),
                "high": float(data.get("h", 0.0)),
                "low": float(data.get("l", 0.0)),
                "open": float(data.get("o", 0.0)),
                "prev_close": float(data.get("pc", 0.0)),
                "timestamp": int(data.get("t", 0) or 0),
            }
        except (TypeError, ValueError) as e:
            raise FinnhubError(f"Failed to normalize quote for {symbol}: {data}") from e

        if normalized["timestamp"] <= 0 or normalized["price"] <= 0:
            raise FinnhubNoDataError(f"No quote data for symbol={symbol}. Raw: {data}")

        self._quote_cache.set(cache_key, normalized, ttl_seconds=15)
        return normalized

    async def get_candles(
        self,
        symbol: str,
        resolution: str,
        from_ts: int,
        to_ts: int,
        timestamp_mode: str = "datetime_utc",
    ) -> pd.DataFrame:
        """
        Finnhub endpoint: /stock/candle

        Must return DataFrame with columns:
          timestamp, open, high, low, close, volume

        timestamp_mode:
          - 'datetime_utc' -> pandas datetime64[ns, UTC]
          - 'epoch' -> int epoch seconds
        """
        symbol = symbol.strip().upper()
        resolution = str(resolution).strip().upper()

        cache_key = ("candles", symbol, resolution, int(from_ts), int(to_ts), timestamp_mode)
        cached = self._candles_cache.get(cache_key)
        if cached is not None:
            return cached.copy()

        raw = await self._request_json(
            "/stock/candle",
            {"symbol": symbol, "resolution": resolution, "from": int(from_ts), "to": int(to_ts)},
        )

        if raw.get("s") != "ok":
            raise FinnhubNoDataError(f"No candle data for symbol={symbol}. Raw: {raw}")

        t = raw.get("t") or []
        o = raw.get("o") or []
        h = raw.get("h") or []
        l = raw.get("l") or []
        c = raw.get("c") or []
        v = raw.get("v") or []

        if not (len(t) == len(o) == len(h) == len(l) == len(c) == len(v)) or len(t) == 0:
            raise FinnhubNoDataError(f"Candle arrays invalid for symbol={symbol}. Raw: {raw}")

        df = pd.DataFrame(
            {"timestamp": t, "open": o, "high": h, "low": l, "close": c, "volume": v}
        )

        df["open"] = pd.to_numeric(df["open"], errors="coerce")
        df["high"] = pd.to_numeric(df["high"], errors="coerce")
        df["low"] = pd.to_numeric(df["low"], errors="coerce")
        df["close"] = pd.to_numeric(df["close"], errors="coerce")
        df["volume"] = pd.to_numeric(df["volume"], errors="coerce")

        if timestamp_mode == "datetime_utc":
            df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s", utc=True)
        elif timestamp_mode == "epoch":
            df["timestamp"] = df["timestamp"].astype("int64")
        else:
            raise ValueError("timestamp_mode must be 'datetime_utc' or 'epoch'")

        df = df.dropna(subset=["open", "high", "low", "close", "volume"]).reset_index(drop=True)
        if df.empty:
            raise FinnhubNoDataError(f"All candle rows invalid after normalization for {symbol}.")

        self._candles_cache.set(cache_key, df.copy(), ttl_seconds=60)
        return df


# ----------------------------------------------------------
# Manual Self-Test
# ----------------------------------------------------------
# Requirements:
#   - FINNHUB_API_KEY set in environment or settings
#
# Example command to test quote + candles:
#
# python -c "import asyncio; from app.data.finnhub_client import FinnhubClient; \
# async def main(): \
#     c=FinnhubClient(); \
#     q=await c.get_quote('AAPL'); \
#     print('QUOTE:', q); \
#     df=await c.get_candles('AAPL','D',1704067200,1706745600); \
#     print(df.tail()); \
#     await c.aclose(); \
# asyncio.run(main())"
#
# Expected result:
#   - Printed normalized quote dictionary
#   - Pandas DataFrame tail with columns:
#       timestamp, open, high, low, close, volume
#
# If the API key or network fails, a FinnhubError will be raised.
