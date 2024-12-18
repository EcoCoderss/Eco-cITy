# tests/test_validation.py

from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_validate_data():
    data = {
        "event_id": 1,
        "capacity": 50000,
        "entrances": 10,
        "exits": 5,
        "risk_factors": ["malore", "scontri"]
    }
    response = client.post("/validate/", json=data)
    assert response.status_code == 200
    assert response.json()["status"] == "success"