from fastapi import APIRouter
from agents.staff_estimation_agent import staff_estimation_agent
from models.staff_estimation import StaffEstimationInput

router = APIRouter()

@router.post("/")
async def simulate_staff_estimation(data: StaffEstimationInput):
    result = staff_estimation_agent.run(data)
    return {"result": result}
