from fastapi import FastAPI
from src.api.routes import router

app = FastAPI()

app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "DataGen WatsonX Microservice is running"}