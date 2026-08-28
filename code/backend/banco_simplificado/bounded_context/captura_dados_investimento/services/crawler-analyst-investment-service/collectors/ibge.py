import httpx
from models.schemas import CollectedData, DataSource
from core.config import settings


# Indicadores macroeconômicos relevantes para análise de investimentos
INDICATORS = {
    "ipca": 7169,       # IPCA acumulado 12 meses
    "pib_trimestral": 1621,  # PIB trimestral
    "desemprego": 6381, # Taxa de desemprego (PNAD)
}


async def collect(params: dict) -> list[CollectedData]:
    results = []
    indicators = params.get("indicators", list(INDICATORS.keys()))

    async with httpx.AsyncClient(timeout=30) as client:
        for name in indicators:
            indicator_id = INDICATORS.get(name)
            if not indicator_id:
                continue

            url = f"{settings.ibge_base_url}/agregados/{indicator_id}/periodos/-1/variaveis"
            response = await client.get(url)
            response.raise_for_status()

            data = response.json()
            results.append(
                CollectedData(
                    source=DataSource.IBGE,
                    payload={
                        "indicator": name,
                        "indicator_id": indicator_id,
                        "data": data,
                    },
                    metadata={"url": url},
                )
            )

    return results
