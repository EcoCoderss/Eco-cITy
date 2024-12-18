from fastapi import FastAPI
from src.api.routes import router  # Importa il router

app = FastAPI()

app.include_router(router)  # Includi il router nell'app

@app.get("/")
def read_root():
    return {"message": "Microservizio di Validazione Attivo"}