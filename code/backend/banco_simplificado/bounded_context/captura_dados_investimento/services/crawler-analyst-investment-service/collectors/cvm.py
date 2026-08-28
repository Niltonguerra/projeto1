import httpx
from models.schemas import CollectedData, DataSource
from core.config import settings


async def collect(params: dict) -> list[CollectedData]:
    results = []

    # Fundos de investimento — dado público da CVM
    url = f"{settings.cvm_base_url}/FI/CAD/DADOS/cad_fi.csv"

    async with httpx.AsyncClient(timeout=60, follow_redirects=True) as client:
        response = await client.get(url)
        response.raise_for_status()

        # Retorna as primeiras linhas do CSV para não sobrecarregar
        lines = response.text.splitlines()
        header = lines[0]
        records = lines[1:101]  # 100 primeiros registros

        results.append(
            CollectedData(
                source=DataSource.CVM,
                payload={
                    "type": "fundos_investimento",
                    "header": header,
                    "records": records,
                    "total_records": len(records),
                },
                metadata={"url": url},
            )
        )

    return results
