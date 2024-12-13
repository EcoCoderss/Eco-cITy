from pydantic import BaseModel

class EmergencyExitInput(BaseModel):
    total_people: int
    building_capacity: int
    evacuation_time_goal: int

class EmergencyExitOutput(BaseModel):
    optimal_exits: int
    time_to_evacuation: float
