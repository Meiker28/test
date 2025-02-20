from fastapi import FastAPI
from datetime import datetime
from pydantic import BaseModel
from typing import Dict

app = FastAPI()
counter = {"count": 0}

class RequestData(BaseModel):
    detailed: bool

@app.post("/get_date")
def get_date(data: RequestData):
    counter["count"] += 1
    now = datetime.now()
    if data.detailed:
        return {"date": now.strftime("%Y-%m-%d %H:%M:%S")}
    else:
        return {"date": now.strftime("%Y-%d-%m")}

@app.get("/counter")
def get_counter():
    return {"count": counter["count"]}