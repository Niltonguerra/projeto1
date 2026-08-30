from modules.health.health_router import health_router
from modules.market_data.market_data_router import market_data_router

def register_routers(app):
    app.include_router(health_router)
    app.include_router(market_data_router)