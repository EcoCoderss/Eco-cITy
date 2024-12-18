from fastapi import APIRouter
from utils.logger import get_logger
from utils.auth import authenticate
from starlette.responses import JSONResponse

router = APIRouter()
logger = get_logger(__name__)

@router.post("/simulate")
@authenticate
async def simulate_event(event_data: dict):
    logger.info("Avvio simulazione evento")
    # Chiamata al servizio di simulazione nell'Event_management
    # response = await call_event_management_service(event_data)
    # return JSONResponse(content=response)
    pass


@router.get("/waste")
def get_waste_data():
    return {"messagfffe": "Waste management data retrieved successfully"}

@router.get("/waste/collect")
def get_waste_data():
    return {" management data retrieved successfully"}


@router.get("/personel")
def get_waste_data():
    return {"messagfffe": "Waste management data retrieved successfully"}

@router.get("/personel/collect")
def get_waste_data():
    return {" management data retrieved successfully"}



@router.get("/event")
def get_waste_data():
    return {"messagfffe": "Waste management data retrieved successfully"}

@router.get("/event/collect")
def get_waste_data():
    return {" management data retrieved successfully"}