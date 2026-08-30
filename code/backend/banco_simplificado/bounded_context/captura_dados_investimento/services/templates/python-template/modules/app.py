from modules.health.router.health_router import health_router

def register_routers(app):
    app.include_router(health_router)