from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_people_flow():
    response = client.post("/people-flow/", json={
        "total_people": 1000,
        "entrances": 3,
        "exits": 5,
        "area": 1500
    })
    assert response.status_code == 200
