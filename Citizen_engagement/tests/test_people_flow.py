from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_people_flow():
    response = client.post("/peopleflow", json={
        "total_people": 1000,
        "entrances": 3,
        "exits": 5,
        "area": 1500
    })
    assert response.status_code == 200
    result = response.json()["result"]
    assert "density" in result
    assert "flow_rate" in result
    assert result["density"] == 1000 / 1500
    assert result["flow_rate"] == 1000 / (3 + 5)
