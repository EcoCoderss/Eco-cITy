from fastapi import APIRouter
from agents.emergency_exit_agent import emergency_exit_agent
from models.emergency_exit import EmergencyExitInput

router = APIRouter()

@router.post("/")
async def simulate_emergency_exit(data: EmergencyExitInput):
    result = emergency_exit_agent.run(data)
    return {"result": result}
