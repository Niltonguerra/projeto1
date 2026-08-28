from pydantic import BaseModel, Field
from typing import Any
from datetime import datetime
from enum import Enum


class DataSource(str, Enum):
    BACEN = "bacen"
    BRAPI = "brapi"
    CVM = "cvm"
    IBGE = "ibge"


class CollectedData(BaseModel):
    """Schema unificado — independente da fonte, todos os dados seguem esse contrato."""
    source: DataSource
    collected_at: datetime = Field(default_factory=datetime.utcnow)
    payload: dict[str, Any]
    metadata: dict[str, Any] = Field(default_factory=dict)


class CollectRequest(BaseModel):
    """Parâmetros opcionais que o Airflow pode enviar ao acionar o endpoint."""
    params: dict[str, Any] = Field(default_factory=dict)


class CollectResponse(BaseModel):
    success: bool
    source: DataSource
    records_collected: int
    data: list[CollectedData]
    error: str | None = None
