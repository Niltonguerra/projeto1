from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from modules.app import register_routers

@asynccontextmanager
async def lifespan(app: FastAPI):
    print(f"Starting app")
    yield
    print("Shutting down...")


app = FastAPI(
    title="Crawler Analyst Investment Service",
    description="Serviço de coleta de dados financeiros e macroeconômicos.",
    lifespan=lifespan,
)

register_routers(app)