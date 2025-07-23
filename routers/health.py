from fastapi import APIRouter, status
from pydantic import BaseModel
from datetime import datetime
import time

router = APIRouter()

# Store application start time
APP_START_TIME = time.time()

class HealthResponse(BaseModel):
    status: str
    timestamp: datetime
    uptime: float
    service: str

@router.get(
    "/health",
    response_model=HealthResponse,
    status_code=status.HTTP_200_OK,
    summary="Health Check",
    description="Returns the health status of the application",
    tags=["Health"]
)
async def health_check():
    """Simple health check - returns 200 if the application is running."""
    return HealthResponse(
        status="healthy",
        timestamp=datetime.utcnow(),
        uptime=time.time() - APP_START_TIME,
        service="kleinanzeigen-api"
    )