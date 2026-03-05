from sqlalchemy import Column, Integer, String, Float, DateTime, JSON
from sqlalchemy.sql import func
from app.db.base import Base

class Stock(Base):
    __tablename__ = "stocks"

    id = Column(Integer, primary_key=True, index=True)
    ticker = Column(String, unique=True, index=True, nullable=False)
    name = Column(String)
    market = Column(String)  # NYSE, NASDAQ, BYMA
    
    # Market Data
    price = Column(Float)
    change_pct = Column(Float)
    volume = Column(Float)
    
    # Intelligence
    score = Column(Integer)  # 0-100
    signal = Column(String)  # BUY, HOLD, SELL
    
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
