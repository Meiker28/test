from typing import Final
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Configuraciones de la aplicación"""

    # Configuraciones de la aplicación
    CACHE_TIME: int = 1  # Segundos para cachear la fecha
    APP_TITLE: str = "API de Fecha y Contador"
    APP_DESCRIPTION: str = "API optimizada para manejo de fechas y conteo de requests"
    APP_VERSION: str = "1.0.0"
    
    class Config:
        case_sensitive = True


def get_settings() -> Settings:
    """
    Obtiene las configuraciones de la aplicación.
    Usa lru_cache para evitar múltiples lecturas.
    """
    return Settings()

# Constantes de la aplicación
settings = get_settings()