from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from datetime import datetime
from schemas import DateFormat, DateRequest, DateResponse, CounterResponse
from config import settings

app = FastAPI(
    title=settings.APP_TITLE,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
    docs_url="/docs",
    redoc_url="/redoc"
)

_request_counter = 0

def get_formatted_date(formato: bool) -> str:

    now = datetime.today()
    formatted_date = now.strftime("%Y-%m-%d %H:%M:%S") if formato else now.strftime("%d-%m-%y")
    return formatted_date 

@app.post(
    "/fecha",
    response_model=DateResponse,
    status_code=status.HTTP_200_OK,
    tags=["Fecha"],
    summary="Obtiene la fecha actual en el formato especificado"
)
async def get_date(request: DateRequest) -> JSONResponse:
    """
    Endpoint para obtener la fecha actual.
    
    Args:
        request: Modelo con el parámetro de formato
    
    Returns:
        JSONResponse con la fecha formateada y el contador.
    """
    global _request_counter
    _request_counter += 1
    
    return JSONResponse(
        content={
            "fecha": get_formatted_date(request.formato),
            "contador": _request_counter
        },
        status_code=status.HTTP_200_OK
    )

@app.get(
    "/contador",
    response_model=CounterResponse,
    status_code=status.HTTP_200_OK,
    tags=["Contador"],
    summary="Obtiene el contador total de requests"
)
async def get_counter() -> JSONResponse:
    """
    Endpoint para obtener el contador de requests.
    
    Returns:
        JSONResponse con el valor actual del contador.
    """
    global _request_counter
    _request_counter += 1
    
    return JSONResponse(
        content={"contador": _request_counter},
        status_code=status.HTTP_200_OK
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app")
