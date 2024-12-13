from fastapi import APIRouter
from agents.people_flow_agent import people_flow_agent
from models.people_flow import PeopleFlowInput

router = APIRouter()

@router.post("/")
async def simulate_people_flow(data: PeopleFlowInput):
    result = people_flow_agent.run(data)
    return {"result": result}
