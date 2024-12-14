from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_people_flow():
    response = client.post("/people-flow/peopleflow/", json={
        "total_people": 1000,
        "entrances": 3,
        "exits": 5,
        "area": 1500
    })
    assert response.status_code == 200
    data = response.json()
    assert "result" in data
    assert data["result"]["density"] == 1000 / 1500
    assert data["result"]["people_per_entrance"] == 1000 / 3
    assert data["result"]["people_per_exit"] == 1000 / 5