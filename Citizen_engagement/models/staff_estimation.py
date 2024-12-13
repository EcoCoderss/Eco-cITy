from pydantic import BaseModel

class StaffEstimationInput(BaseModel):
    event_type: str
    audience_size: int
    risk_level: str
    duration_hours: int

class StaffEstimationOutput(BaseModel):
    stewards: int
    paramedics: int
    police: int
