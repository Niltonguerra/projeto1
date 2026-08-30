from fastapi import APIRouter
from core.config import settings

health_router = APIRouter()

@health_router.get("/health")
async def health():
    return {"status": "ok", "service": settings.app_name}