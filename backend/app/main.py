from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.settings import settings
from app.routes import health, stocks
from app.core.logging import logger

def get_application() -> FastAPI:
    application = FastAPI(
        title=settings.PROJECT_NAME,
        openapi_url=f"{settings.API_V1_STR}/openapi.json"
    )

    # Set all CORS enabled origins
    if settings.BACKEND_CORS_ORIGINS:
        application.add_middleware(
            CORSMiddleware,
            allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    # Include routers
    application.include_router(health.router, prefix=settings.API_V1_STR, tags=["health"])
    application.include_router(stocks.router, prefix=settings.API_V1_STR)

    return application

app = get_application()

@app.on_event("startup")
async def startup_event():
    logger.info("Starting up ARGOS Backend...")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down ARGOS Backend...")
