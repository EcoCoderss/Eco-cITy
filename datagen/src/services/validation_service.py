# src/services/validation_service.py

from src.models.event_model import EventData

def validate_event_data(data: EventData):
    event = EventData(**data.model_dump())
    return {"status": "success", "data": event}