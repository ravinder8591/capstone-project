from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_predict_all():
    r = client.post("/predict", json={})
    assert r.status_code == 200
    assert "predictions" in r.json()