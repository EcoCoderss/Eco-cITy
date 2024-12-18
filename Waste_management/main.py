from fastapi import FastAPI
from routes import simulation  # Importa il router principale

app = FastAPI(title="Waste Management Service", version="1.0")

# Aggiungi i router delle API
app.include_router(simulation.router, prefix="/waste", tags=["waste"])

@app.get("/waste")
def get_waste_data():
    return {"message": "Waste Management Data"}

@app.post("/waste/collect")
def collect_waste(data: dict):
    return {"message": "Waste collected successfully", "data": data}
