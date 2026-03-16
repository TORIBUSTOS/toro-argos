from __future__ import annotations

import time
from collections import Counter
from statistics import mean
from typing import Any, Dict, List, Optional

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.data.universe import get_universe
from app.data.finnhub_client import FinnhubClient, FinnhubNoDataError, FinnhubError
from app.db.models import Stock
from app.db.session import get_db
from app.services.market_scanner import scan_universe, scan_universe_and_persist
from app.services.signal_engine import compute_signal_dict

router = APIRouter(prefix="/stocks", tags=["stocks"])


def _strip_candles(results: list) -> list:
    """Remove candles key from scan results (not JSON-serializable)."""
    return [{k: v for k, v in r.items() if k != "candles"} for r in results]


def _serialize_stock_row(row: Stock) -> Dict[str, Any]:
    return {
        "ticker": row.ticker,
        "market": row.market,
        "price": row.price,
        "signal": row.signal,
        "score": row.score,
        "indicators": row.indicators,
        "updated_at": getattr(row, "updated_at", None),
        "change_pct": getattr(row, "change_pct", None),
        "reason": getattr(row, "reason", None),
    }


def _base_stock_query(db: Session):
    return db.query(Stock)


@router.get("/universe")
async def get_universe_list() -> Dict[str, Any]:
    """Return the canonical ARGOS universe (TORO100)."""
    assets = get_universe("TORO100")
    return {
        "mode": "TORO100",
        "count": len(assets),
        "assets": assets,
    }


@router.get("/scan")
async def scan_market(
    persist: bool = Query(False, description="Persist scan results into database"),
    db: Session = Depends(get_db),
) -> Dict[str, Any]:
    """Run a full TORO100 scan. If persist=true, UPSERTs results into Stock table."""
    started_at = int(time.time())

    try:
        if persist:
            payload = await scan_universe_and_persist(db)
            payload["started_at"] = started_at
            payload["results"] = _strip_candles(payload["results"])
            return payload

        results = await scan_universe()
    except FinnhubError as e:
        raise HTTPException(status_code=503, detail=str(e))

    ok = sum(1 for r in results if "error" not in r)
    failed = len(results) - ok

    return {
        "mode": "TORO100",
        "count": len(results),
        "ok": ok,
        "failed": failed,
        "started_at": started_at,
        "results": _strip_candles(results),
    }


@router.get("/latest")
async def latest(
    limit: int = Query(100, ge=1, le=500),
    signal: Optional[str] = Query(None, description="Filter: BUY / HOLD / SELL"),
    market: Optional[str] = Query(None, description="Filter: US / BYMA"),
    db: Session = Depends(get_db),
) -> Dict[str, Any]:
    """Return latest persisted stock states from DB."""
    q = db.query(Stock)

    if signal:
        q = q.filter(Stock.signal == signal.strip().upper())
    if market:
        q = q.filter(Stock.market == market.strip().upper())

    q = q.order_by(Stock.updated_at.desc())
    rows = q.limit(limit).all()

    items = [
        {
            "ticker": row.ticker,
            "market": row.market,
            "price": row.price,
            "change_pct": row.change_pct,
            "signal": row.signal,
            "score": row.score,
            "indicators": row.indicators,
            "reason": row.reason,
            "updated_at": row.updated_at.isoformat() if row.updated_at else None,
        }
        for row in rows
    ]

    return {
        "count": len(items),
        "items": items,
    }


@router.get("/asset/{ticker}")
async def get_asset_detail(
    ticker: str,
    market: str = Query("US", description="Market hint: US or BYMA"),
    resolution: str = Query("D", description="Candle resolution (D, W, 60)"),
    days: int = Query(120, ge=30, le=365, description="Lookback window in days"),
) -> Dict[str, Any]:
    """Return quote, candles and signal pack for a single asset."""
    ticker = ticker.strip().upper()
    market = market.strip().upper()

    client = FinnhubClient()
    try:
        now = int(time.time())
        from_ts = now - (60 * 60 * 24 * days)

        quote = await client.get_quote(ticker)
        candles = await client.get_candles(
            ticker,
            resolution=resolution,
            from_ts=from_ts,
            to_ts=now,
            timestamp_mode="epoch",
        )
        signal_pack = compute_signal_dict(candles)

        return {
            "ticker": ticker,
            "market": market,
            "quote": quote,
            "signal": signal_pack["signal"],
            "score": signal_pack["score"],
            "indicators": signal_pack["indicators"],
            "reason": signal_pack["reason"],
            "candles_count": len(candles),
            "candles": candles.to_dict(orient="records"),
        }
    except FinnhubNoDataError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except FinnhubError as e:
        raise HTTPException(status_code=502, detail=str(e))
    finally:
        await client.aclose()


@router.get("/top-buy")
async def top_buy(
    limit: int = Query(10, ge=1, le=100),
    market: Optional[str] = Query(None, description="Optional filter: US / BYMA"),
    db: Session = Depends(get_db),
) -> Dict[str, Any]:
    """
    Returns top persisted BUY candidates ordered by:
    1) score desc
    2) change_pct desc if available
    3) ticker asc
    """
    q = _base_stock_query(db).filter(Stock.signal == "BUY")

    if market:
        q = q.filter(Stock.market == market.strip().upper())

    if hasattr(Stock, "change_pct"):
        q = q.order_by(Stock.score.desc(), Stock.change_pct.desc(), Stock.ticker.asc())
    else:
        q = q.order_by(Stock.score.desc(), Stock.ticker.asc())

    rows = q.limit(limit).all()

    return {
        "count": len(rows),
        "items": [_serialize_stock_row(r) for r in rows],
    }


@router.get("/top-sell")
async def top_sell(
    limit: int = Query(10, ge=1, le=100),
    market: Optional[str] = Query(None, description="Optional filter: US / BYMA"),
    db: Session = Depends(get_db),
) -> Dict[str, Any]:
    """
    Returns top persisted SELL candidates ordered by:
    1) score asc
    2) change_pct asc if available
    3) ticker asc
    """
    q = _base_stock_query(db).filter(Stock.signal == "SELL")

    if market:
        q = q.filter(Stock.market == market.strip().upper())

    if hasattr(Stock, "change_pct"):
        q = q.order_by(Stock.score.asc(), Stock.change_pct.asc(), Stock.ticker.asc())
    else:
        q = q.order_by(Stock.score.asc(), Stock.ticker.asc())

    rows = q.limit(limit).all()

    return {
        "count": len(rows),
        "items": [_serialize_stock_row(r) for r in rows],
    }


@router.get("/summary")
async def summary(
    db: Session = Depends(get_db),
) -> Dict[str, Any]:
    """
    Returns a compact executive summary of persisted market state.
    Useful for dashboard cards / radar overview.
    """
    rows: List[Stock] = _base_stock_query(db).all()

    if not rows:
        return {
            "count": 0,
            "signals": {"BUY": 0, "HOLD": 0, "SELL": 0},
            "markets": {},
            "avg_score": None,
            "top_buy": [],
            "top_sell": [],
            "last_updated_at": None,
        }

    signal_counts = Counter((r.signal or "UNKNOWN") for r in rows)
    market_counts = Counter((r.market or "UNKNOWN") for r in rows)

    scores = [r.score for r in rows if r.score is not None]
    avg_score = round(mean(scores), 2) if scores else None

    updated_values = [getattr(r, "updated_at", None) for r in rows if getattr(r, "updated_at", None) is not None]
    last_updated_at = max(updated_values) if updated_values else None

    buy_rows = [r for r in rows if r.signal == "BUY"]
    sell_rows = [r for r in rows if r.signal == "SELL"]

    def sort_buy_key(r: Stock):
        cp = getattr(r, "change_pct", None)
        return (
            -(r.score if r.score is not None else -999),
            -(cp if cp is not None else -999999),
            r.ticker or "",
        )

    def sort_sell_key(r: Stock):
        cp = getattr(r, "change_pct", None)
        return (
            (r.score if r.score is not None else 999),
            (cp if cp is not None else 999999),
            r.ticker or "",
        )

    top_buy_rows = sorted(buy_rows, key=sort_buy_key)[:5]
    top_sell_rows = sorted(sell_rows, key=sort_sell_key)[:5]

    return {
        "count": len(rows),
        "signals": {
            "BUY": signal_counts.get("BUY", 0),
            "HOLD": signal_counts.get("HOLD", 0),
            "SELL": signal_counts.get("SELL", 0),
        },
        "markets": dict(market_counts),
        "avg_score": avg_score,
        "last_updated_at": last_updated_at,
        "top_buy": [_serialize_stock_row(r) for r in top_buy_rows],
        "top_sell": [_serialize_stock_row(r) for r in top_sell_rows],
    }
