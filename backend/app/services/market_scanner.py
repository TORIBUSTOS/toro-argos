from __future__ import annotations

import time
from typing import Any, Dict, List, Optional

from sqlalchemy.orm import Session

from app.data.universe import get_universe
from app.data.finnhub_client import FinnhubClient
from app.services.signal_engine import compute_signal_dict
from app.db.models import Stock


async def scan_universe() -> List[Dict[str, Any]]:
    """
    ARGOS Market Scanner

    Steps:
    1. Load TORO100
    2. Fetch quote
    3. Fetch candles
    4. Compute signal pack
    5. Return normalized dataset
    """
    client = FinnhubClient()
    universe = get_universe("TORO100")
    results: List[Dict[str, Any]] = []

    now = int(time.time())
    from_ts = now - (60 * 60 * 24 * 120)

    try:
        for asset in universe:
            ticker = asset["ticker"]
            market = asset["market"]

            try:
                quote = await client.get_quote(ticker)
                candles = await client.get_candles(
                    ticker,
                    resolution="D",
                    from_ts=from_ts,
                    to_ts=now,
                )
                signal_pack = compute_signal_dict(candles)

                results.append(
                    {
                        "ticker": ticker,
                        "market": market,
                        "price": quote["price"],
                        "change_pct": quote["change_pct"],
                        "signal": signal_pack["signal"],
                        "score": signal_pack["score"],
                        "indicators": signal_pack["indicators"],
                        "reason": signal_pack["reason"],
                        "candles": candles,
                    }
                )
            except Exception as e:
                results.append(
                    {
                        "ticker": ticker,
                        "market": market,
                        "error": str(e),
                    }
                )
    finally:
        await client.aclose()

    return results


def _upsert_stock_row(db: Session, item: Dict[str, Any]) -> Stock:
    """Upsert latest scan result into Stock table using (ticker, market) identity."""
    ticker = item["ticker"]
    market = item["market"]

    existing: Optional[Stock] = (
        db.query(Stock)
        .filter(Stock.ticker == ticker, Stock.market == market)
        .first()
    )

    if existing:
        existing.price = item.get("price")
        existing.change_pct = item.get("change_pct")
        existing.signal = item.get("signal")
        existing.score = item.get("score")
        existing.indicators = item.get("indicators")
        existing.reason = item.get("reason")
        return existing

    row = Stock(
        ticker=ticker,
        market=market,
        price=item.get("price"),
        change_pct=item.get("change_pct"),
        signal=item.get("signal"),
        score=item.get("score"),
        indicators=item.get("indicators"),
        reason=item.get("reason"),
    )
    db.add(row)
    return row


async def scan_universe_and_persist(db: Session) -> Dict[str, Any]:
    """
    Run full scan and persist successful results into DB.
    Failed items are returned but not persisted.
    """
    results = await scan_universe()

    ok = 0
    failed = 0
    for item in results:
        if "error" in item:
            failed += 1
            continue
        _upsert_stock_row(db, item)
        ok += 1

    db.commit()

    return {
        "mode": "TORO100",
        "count": len(results),
        "ok": ok,
        "failed": failed,
        "persisted": ok,
        "results": results,
    }
