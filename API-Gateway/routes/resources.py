from fastapi import APIRouter
from utils.auth import authenticate

router = APIRouter()

@router.get("/resources")
@authenticate
async def get_resources():
    # Logica per ottenere le risorse disponibili
    pass