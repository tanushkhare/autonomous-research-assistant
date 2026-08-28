import pytest
from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "healthy"

def test_research_query():
    payload = {"topic": "Distributed Consensus Raft", "depth_level": "deep"}
    res = client.post("/api/v1/research/query", json=payload)
    assert res.status_code == 200
    data = res.json()
    assert "RES-" in data["research_id"]
    assert len(data["citations"]) > 0
    assert data["citations"][0]["relevance_score"] > 0.8
