from __future__ import annotations

from typing import Dict, List, Literal, Tuple


Market = Literal["US", "BYMA"]


"""
TORO100 (CANON)
ARGOS watches 100 assets = 100 ojos.
Split:
- 60 US (subyacentes CEDEAR / USA)
- 40 BYMA (Argentina)

Rules:
- EXACT length: 100
- Deterministic order (list order is canon)
- No duplicates inside each market
- Output format: [{"ticker": "...", "market": "US"|"BYMA"}, ...]
"""


TORO100_US: List[str] = [
    # Mega/Tech
    "AAPL","MSFT","GOOGL","AMZN","META","NVDA","TSLA","NFLX","ORCL","IBM",
    # Semis / HW
    "AMD","INTC","AVGO","QCOM","TXN","MU","ASML","TSM","AMAT","LRCX",
    # Payments / Fintech
    "V","MA","PYPL","SQ","AXP",
    # Consumer / Retail
    "WMT","COST","KO","PEP","MCD","NKE","DIS","SBUX","TGT","HD",
    # Healthcare
    "JNJ","PFE","MRK","UNH","ABBV",
    # Energy / Industrials
    "XOM","CVX","BA","CAT","GE","MMM",
    # ETFs (barometers)
    "SPY","QQQ","IWM","DIA","XLK",
    # LatAm / EM (CEDEAR common)
    "MELI","BABA","VALE","PBR","NU",
    # Additional to reach 60
    "PG","UNP","VZ","CRM",
]

TORO100_BYMA: List[str] = [
    # Financials
    "GGAL","BMA","SUPV","BBAR","BYMA",
    # Energy / Utilities
    "YPFD","PAMP","TGNO4","TGSU2","CEPU","TRAN","EDN",
    # Materials / Industrials
    "ALUA","TXAR","COME","LOMA","MIRG",
    # Agro / Consumer / Holding
    "CRES","AGRO","MOLI","LEDE","IRSA",
    # Telecom / Media
    "TECO2","CVH",
    # Others / Liquidity staples
    "VALO","SAMI","METR","CAPX","DGCU2","HARG","OEST","BOLT",
    # Extra slots to reach 40 (can curate later, keep deterministic)
    "AUSO","MTR","INVJ","FERR","GARO",
    # Additional to reach 40
    "MORI","GCLA","LECO",
]

# -----------------------------
# Validation helpers
# -----------------------------

def _norm(t: str) -> str:
    return t.strip().upper()


def _assert_unique(seq: List[str], label: str) -> None:
    seen = set()
    dups = []
    for x in seq:
        nx = _norm(x)
        if nx in seen:
            dups.append(nx)
        seen.add(nx)
    if dups:
        raise RuntimeError(f"Universe list '{label}' has duplicates: {sorted(set(dups))}")


def _build_toro100() -> List[Dict[str, str]]:
    us = [_norm(t) for t in TORO100_US]
    byma = [_norm(t) for t in TORO100_BYMA]

    # Strict: expected sizes
    if len(us) != 60:
        raise RuntimeError(f"TORO100_US must have 60 tickers, got {len(us)}")
    if len(byma) != 40:
        raise RuntimeError(f"TORO100_BYMA must have 40 tickers, got {len(byma)}")

    _assert_unique(us, "TORO100_US")
    _assert_unique(byma, "TORO100_BYMA")

    universe: List[Dict[str, str]] = [{"ticker": t, "market": "US"} for t in us] + \
                                     [{"ticker": t, "market": "BYMA"} for t in byma]

    if len(universe) != 100:
        raise RuntimeError(f"TORO100 must be exactly 100 assets, got {len(universe)}")

    return universe


def get_universe(mode: str = "TORO100") -> List[Dict[str, str]]:
    """
    mode supported:
      - TORO100
    """
    m = _norm(mode)
    if m != "TORO100":
        raise ValueError("Only mode='TORO100' is supported in MVP.")
    return _build_toro100()


# Optional quick check (manual):
# python -c "from app.data.universe import get_universe; u=get_universe(); print(len(u), u[0], u[-1])"
