from enum import Enum
from pydantic import BaseModel
from fastapi import Body

class DateFormat(str, Enum):
    """Enum para definir los formatos de fecha disponibles"""
    FULL = "%Y-%m-%d %H:%M:%S"
    SHORT = "%Y-%d-%m"

class DateRequest(BaseModel):
    """Modelo Pydantic para validar el request"""
    formato: bool = Body(
        ...,
        description="True para formato completo (aaaa-mm-dd hh:ii:ss), False para formato corto (aaaa-dd-mm)"
    )

class DateResponse(BaseModel):
    """Modelo Pydantic para la respuesta del endpoint de fecha"""
    fecha: str
    contador: int

class CounterResponse(BaseModel):
    """Modelo Pydantic para la respuesta del endpoint de contador"""
    contador: int