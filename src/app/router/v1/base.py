from fastapi import APIRouter
from .exchange_rate import router as exchange_rate_router

router = APIRouter()

router.include_router(exchange_rate_router, prefix="/api/v1")
