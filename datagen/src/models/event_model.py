# src/models/event_model.py

from pydantic import BaseModel
from typing import List

class EventData(BaseModel):
    event_id: int
    capacity: int
    entrances: int
    exits: int
    risk_factors: List[str]