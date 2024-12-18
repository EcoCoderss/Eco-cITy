from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_send_to_watsonx():
    data = {
        # Dati di esempio per il test
    }
    response = client.post("/send-to-watsonx/", json=data)
    assert response.status_code == 200
    assert response.json()["status"] == "success"