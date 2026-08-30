# modules/market_data/routes/quote_router.py
from fastapi import APIRouter
from modules.market_data.controllers.quote_controller import quote_controller

quote_router = APIRouter(prefix="/quote")

@quote_router.get("/teste/{ticker}")
async def get_quote(ticker: str):
    return await quote_controller.get_quote(ticker)