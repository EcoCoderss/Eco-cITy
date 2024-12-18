from fastapi import FastAPI
from routes import simulation, resources
from utils.logger import get_logger
from routes.resources import router as resources_router
from routes.simulation import router as simulation_router
import httpx

app = FastAPI(title="ECO-CITY API Gateway", version="1.0")
logger = get_logger(__name__)

app.include_router(simulation.router)
app.include_router(resources.router)
# Includi il router con prefisso "/waste"
app.include_router(simulation.router, prefix="/waste", tags=["waste"])
app.include_router(simulation.router, prefix="/waste/collect", tags=["waste"])
app.include_router(simulation.router, prefix="/personel", tags=["personel"])
app.include_router(simulation.router, prefix="/personel/collect", tags=["personel"])
app.include_router(simulation.router, prefix="/event", tags=["event"])
app.include_router(simulation.router, prefix="/event/collect", tags=["event"])

if __name__ == "__main__":
    import uvicorn
    logger.info("Starting API Gateway...")
    uvicorn.run(app, host="0.0.0.0", port=8000)


    # Servizio Waste Management
@app.get("/api/waste")
async def get_waste_data():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://127.0.0.1:8000/waste")
    return response.json()

@app.post("/api/waste/collect")
async def collect_waste(data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post("http://127.0.0.1:8000/waste/collect", json=data)
    return response.json()



    # Servizio personel Management
@app.get("/api/personel")
async def get_waste_data():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://127.0.0.1:8000/personel")
    return response.json()

@app.post("/api/personel/collect")
async def collect_waste(data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post("http://127.0.0.1:8000/personel/collect", json=data)
    return response.json()

    # Servizio Event Management
@app.get("/api/event")
async def get_waste_data():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://127.0.0.1:8000/event")
    return response.json()

@app.post("/api/event/collect")
async def collect_waste(data: dict):
    async with httpx.AsyncClient() as client:
        response = await client.post("http://127.0.0.1:8000/event/collect", json=data)
    return response.json()

