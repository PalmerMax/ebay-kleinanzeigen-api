import logging
import os
from fastapi import FastAPI
from contextlib import asynccontextmanager
from config import settings
from routers import inserate, inserat, health

LOG_FORMAT_APP = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format=LOG_FORMAT_APP,
        force=True  # This replaces any existing configuration
    )

setup_logging()

app_logger = logging.getLogger("kleinanzeigen")

@asynccontextmanager
async def lifespan(app: FastAPI):
    app_logger.info("Validating environment variables for startup")
    required_envs = ["EBAY_API_PORT", "EBAY_API_HOST"]
    for env_var in required_envs:
        if os.environ.get(env_var) is None:
            raise RuntimeError(f"Environment variable {env_var} must be set.")
    app_logger.info(f"Starting Kleinanzeigen API on {settings.ebay_api_host}:{settings.ebay_api_port}")
    yield
    app_logger.info("Shutting down Kleinanzeigen API")

app = FastAPI(version="1.0.0", lifespan=lifespan)

@app.get("/")
async def root():
    return {
        "message": "Welcome to the Kleinanzeigen API",
        "endpoints": ["/inserate", "/inserat/{id}", "/health"]
    }

app.include_router(inserate.router)
app.include_router(inserat.router)
app.include_router(health.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=settings.ebay_api_host,
        port=settings.ebay_api_port,
        log_config=None  # Disable uvicorn's logging config, use Python's logging
    )