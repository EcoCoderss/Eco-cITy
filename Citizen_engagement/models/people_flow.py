from pydantic import BaseModel

class PeopleFlowInput(BaseModel):
    total_people: int
    entrances: int
    exits: int
    area: float

class PeopleFlowOutput(BaseModel):
    evacuation_time: float
    crowd_density: str
