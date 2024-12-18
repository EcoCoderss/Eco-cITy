from fastapi import FastAPI
from routes import simulation  # Importa il router principale

app = FastAPI(title="event Management Service", version="1.0")

# Aggiungi i router delle API
app.include_router(simulation.router, prefix="/event", tags=["event"])

@app.get("/event")
def get_waste_data():
    return {"message": "event Management Data"}

@app.post("/event/collect")
def collect_waste(data: dict):
    return {"message": "event collected successfully", "data": data}
