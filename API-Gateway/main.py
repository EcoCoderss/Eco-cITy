from fastapi import FastAPI
from routes import simulation, resources
from utils.logger import get_logger

app = FastAPI()
logger = get_logger(__name__)

app.include_router(simulation.router)
app.include_router(resources.router)

if __name__ == "__main__":
    import uvicorn
    logger.info("Starting API Gateway...")
    uvicorn.run(app, host="0.0.0.0", port=8000)