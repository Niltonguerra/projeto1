from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "crawler-analyst-investment-service"
    app_version: str = "1.0.0"
    port: int = 3500

    # Brapi (única que exige token)
    brapi_base_url: str = "https://brapi.dev/api"
    brapi_token: str = ""

    # Banco Central
    bacen_base_url: str = "https://api.bcb.gov.br/dados/serie/bcdata.sgs"

    # CVM
    cvm_base_url: str = "https://dados.cvm.gov.br/dados"

    # IBGE
    ibge_base_url: str = "https://servicodados.ibge.gov.br/api/v3"

    class Config:
        env_file = ".env"


settings = Settings()
