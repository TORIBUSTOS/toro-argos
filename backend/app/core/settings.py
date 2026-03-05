from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    # API configuration
    API_V1_STR: str = "/api"
    PROJECT_NAME: str = "ARGOS Backend"
    
    # Environment variables
    FINNHUB_API_KEY: str
    DATABASE_URL: str
    LOG_LEVEL: str = "INFO"
    UPDATE_CRON: str = "0 0 * * *"
    TIMEZONE: str = "America/Argentina/Buenos_Aires"
    
    # CORS
    BACKEND_CORS_ORIGINS: list[str] = [
        "http://localhost:3000",
        "http://localhost:8000",
    ]

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True
    )

settings = Settings()
