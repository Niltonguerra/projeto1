from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager

from core.config import settings
from models.schemas import CollectRequest, CollectResponse, DataSource
from collectors import bacen, brapi, cvm, ibge


@asynccontextmanager
async def lifespan(app: FastAPI):
    print(f"Starting {settings.app_name} v{settings.app_version}")
    yield
    print("Shutting down...")


app = FastAPI(
    title="Crawler Analyst Investment Service",
    description="Serviço de coleta de dados financeiros e macroeconômicos.",
    version=settings.app_version,
    lifespan=lifespan,
)

# Mapa de fonte → coletor
COLLECTORS = {
    DataSource.BACEN: bacen.collect,
    DataSource.BRAPI: brapi.collect,
    DataSource.CVM: cvm.collect,
    DataSource.IBGE: ibge.collect,
}


@app.get("/health")
async def health():
    return {"status": "ok", "service": settings.app_name}


@app.post("/collect/{source}", response_model=CollectResponse)
async def collect(source: DataSource, body: CollectRequest = CollectRequest()):
    """
    Endpoint acionado pelo Airflow para coletar dados de uma fonte específica.
    - source: bacen | brapi | cvm | ibge
    - body.params: parâmetros opcionais (tickers, series, indicators, etc.)
    """
    collector = COLLECTORS.get(source)
    if not collector:
        raise HTTPException(status_code=404, detail=f"Source '{source}' not found.")

    try:
        data = await collector(body.params)
        return CollectResponse(
            success=True,
            source=source,
            records_collected=len(data),
            data=data,
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=CollectResponse(
                success=False,
                source=source,
                records_collected=0,
                data=[],
                error=str(e),
            ).model_dump(),
        )


@app.post("/collect/all", response_model=list[CollectResponse])
async def collect_all(body: CollectRequest = CollectRequest()):
    """
    Coleta de todas as fontes de uma vez.
    Útil para o Airflow acionar tudo em paralelo numa única chamada.
    """
    responses = []
    for source, collector in COLLECTORS.items():
        try:
            data = await collector(body.params)
            responses.append(
                CollectResponse(
                    success=True,
                    source=source,
                    records_collected=len(data),
                    data=data,
                )
            )
        except Exception as e:
            responses.append(
                CollectResponse(
                    success=False,
                    source=source,
                    records_collected=0,
                    data=[],
                    error=str(e),
                )
            )
    return responses
