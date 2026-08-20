import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "healthy"

def test_research_cycle():
    payload = {"topic": "Zero Trust Security Architectures", "depth_level": "Technical"}
    res = client.post("/api/v1/research/execute", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert "task_id" in data
    assert len(data["detailed_findings"]) > 0
    assert len(data["strategic_recommendations"]) > 0
