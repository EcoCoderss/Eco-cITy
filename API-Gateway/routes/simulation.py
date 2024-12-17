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