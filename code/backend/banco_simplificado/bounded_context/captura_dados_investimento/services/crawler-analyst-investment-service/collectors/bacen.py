import httpx
from models.schemas import CollectedData, DataSource
from core.config import settings


# Séries mais relevantes para análise de investimentos
SERIES = {
    "selic": 11,        # Taxa Selic
    "ipca": 433,        # IPCA mensal
    "cambio_usd": 1,    # Câmbio USD/BRL
    "pib": 4380,        # PIB mensal
}


async def collect(params: dict) -> list[CollectedData]:
    results = []
    series_ids = params.get("series", list(SERIES.keys()))

    async with httpx.AsyncClient(timeout=30) as client:
        for name in series_ids:
            serie_id = SERIES.get(name)
            if not serie_id:
                continue

            url = f"{settings.bacen_base_url}.{serie_id}/dados/ultimos/1"
            response = await client.get(url, params={"formato": "json"})
            response.raise_for_status()

            data = response.json()
            results.append(
                CollectedData(
                    source=DataSource.BACEN,
                    payload={"serie": name, "serie_id": serie_id, "data": data},
                    metadata={"url": url},
                )
            )

    return results
