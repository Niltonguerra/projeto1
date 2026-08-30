# modules/market_data/market_data_router.py
from fastapi import APIRouter
from modules.market_data.routes.quote_router import quote_router

market_data_router = APIRouter(prefix="/market_data")

market_data_router.include_router(quote_router)
