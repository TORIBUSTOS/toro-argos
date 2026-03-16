from sqlalchemy import Column, Integer, String, Float, DateTime, JSON, UniqueConstraint
from sqlalchemy.sql import func
from app.db.base import Base

class Stock(Base):
    __tablename__ = "stocks"
    __table_args__ = (
        UniqueConstraint("ticker", "market", name="uq_stock_ticker_market"),
    )

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String, index=True, nullable=False)
    name = Column(String)
    market = Column(String, index=True)  # US, BYMA

    # Market Data
    price = Column(Float)
    change_pct = Column(Float)
    volume = Column(Float)

    # Intelligence
    score = Column(Integer)
    signal = Column(String, index=True)  # BUY, HOLD, SELL
    reason = Column(String)

    # Indicators (JSON for flexibility in MVP)
    indicators = Column(JSON)

    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Watchlist(Base):
    __tablename__ = "watchlist"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)  # Future-proofing for auth
    ticker = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
