from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Any, Optional

import pandas as pd


@dataclass(frozen=True)
class SignalResult:
    signal: str          # "BUY" | "HOLD" | "SELL"
    score: int           # -3..+3 (MVP)
    indicators: Dict[str, Any]
    reason: str


def _rsi(series: pd.Series, period: int = 14) -> pd.Series:
    """
    RSI (Wilder) computed with simple rolling means (MVP).
    Returns a Series aligned with input.
    """
    delta = series.diff()
    gain = delta.clip(lower=0)
    loss = (-delta).clip(lower=0)

    avg_gain = gain.rolling(window=period, min_periods=period).mean()
    avg_loss = loss.rolling(window=period, min_periods=period).mean()

    rs = avg_gain / avg_loss.replace(0, pd.NA)
    rsi = 100 - (100 / (1 + rs))
    return rsi


def compute_signal(
    candles: pd.DataFrame,
    *,
    rsi_period: int = 14,
    sma_fast: int = 20,
    sma_slow: int = 50,
    momentum_days: int = 10,
) -> SignalResult:
    """
    Input candles DataFrame columns expected:
      timestamp, open, high, low, close, volume
    timestamp can be datetime or epoch; only 'close' is required for indicators.
    """

    if candles is None or candles.empty:
        return SignalResult(
            signal="HOLD",
            score=0,
            indicators={},
            reason="No candles data.",
        )

    df = candles.copy()

    # Ensure close numeric
    df["close"] = pd.to_numeric(df["close"], errors="coerce")
    df = df.dropna(subset=["close"]).reset_index(drop=True)

    # Need enough rows for slow SMA at least
    min_needed = max(rsi_period + 1, sma_slow + 1, momentum_days + 1)
    if len(df) < min_needed:
        return SignalResult(
            signal="HOLD",
            score=0,
            indicators={"rows": len(df), "min_needed": min_needed},
            reason=f"Insufficient candles rows ({len(df)}/{min_needed}).",
        )

    close = df["close"]

    rsi = _rsi(close, period=rsi_period)
    sma20 = close.rolling(window=sma_fast, min_periods=sma_fast).mean()
    sma50 = close.rolling(window=sma_slow, min_periods=sma_slow).mean()

    # Momentum: % change vs N days ago
    mom = (close / close.shift(momentum_days) - 1.0) * 100.0

    # Latest values
    last_close = float(close.iloc[-1])
    last_rsi = float(rsi.iloc[-1]) if pd.notna(rsi.iloc[-1]) else None
    last_sma20 = float(sma20.iloc[-1]) if pd.notna(sma20.iloc[-1]) else None
    last_sma50 = float(sma50.iloc[-1]) if pd.notna(sma50.iloc[-1]) else None
    last_mom = float(mom.iloc[-1]) if pd.notna(mom.iloc[-1]) else None

    # Scoring (MVP, interpretable)
    score = 0
    reasons = []

    # Trend score via SMA relationship + price position
    if last_sma20 is not None and last_sma50 is not None:
        if last_sma20 > last_sma50:
            score += 1
            reasons.append("SMA20>SMA50 (uptrend)")
        elif last_sma20 < last_sma50:
            score -= 1
            reasons.append("SMA20<SMA50 (downtrend)")

        if last_close > last_sma20:
            score += 1
            reasons.append("Price>SMA20 (strength)")
        elif last_close < last_sma20:
            score -= 1
            reasons.append("Price<SMA20 (weakness)")

    # RSI score (avoid catching falling knives blindly)
    if last_rsi is not None:
        if last_rsi <= 30:
            score += 1
            reasons.append("RSI<=30 (oversold)")
        elif last_rsi >= 70:
            score -= 1
            reasons.append("RSI>=70 (overbought)")

    # Momentum score
    if last_mom is not None:
        if last_mom >= 2.0:
            score += 1
            reasons.append(f"Momentum {momentum_days}d >= +2%")
        elif last_mom <= -2.0:
            score -= 1
            reasons.append(f"Momentum {momentum_days}d <= -2%")

    # Clamp score to [-3, +3]
    score = max(-3, min(3, score))

    # Convert score -> signal (MVP thresholds)
    # +2/+3 => BUY, -2/-3 => SELL else HOLD
    if score >= 2:
        signal = "BUY"
    elif score <= -2:
        signal = "SELL"
    else:
        signal = "HOLD"

    indicators: Dict[str, Any] = {
        "close": last_close,
        "rsi": last_rsi,
        "sma20": last_sma20,
        "sma50": last_sma50,
        "momentum_pct": last_mom,
        "score": score,
    }

    reason = "; ".join(reasons) if reasons else "Neutral."

    return SignalResult(
        signal=signal,
        score=score,
        indicators=indicators,
        reason=reason,
    )


def compute_signal_dict(candles: pd.DataFrame) -> Dict[str, Any]:
    """
    Convenience wrapper: returns plain dict (easy to serialize).
    """
    res = compute_signal(candles)
    return {
        "signal": res.signal,
        "score": res.score,
        "indicators": res.indicators,
        "reason": res.reason,
    }
