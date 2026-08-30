import httpx
from models.schemas import CollectedData, DataSource
from core.config import settings


DEFAULT_TICKERS = ["PETR4", "VALE3", "ITUB4", "BBDC4", "ABEV3"]


async def collect(params: dict) -> list[CollectedData]:
    tickers = params.get("tickers", DEFAULT_TICKERS)
    results = []

    headers = {}
    if settings.brapi_token:
        headers["Authorization"] = f"Bearer {settings.brapi_token}"

    async with httpx.AsyncClient(timeout=30) as client:
        for ticker in tickers:
            url = f"{settings.brapi_base_url}/quote/{ticker}"
            response = await client.get(url, headers=headers)
            response.raise_for_status()

            data = response.json()
            results.append(
                CollectedData(
                    source=DataSource.BRAPI,
                    payload={"ticker": ticker, "data": data},
                    metadata={"url": url},
                )
            )

    return results
