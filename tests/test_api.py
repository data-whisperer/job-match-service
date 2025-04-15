"""
Tests for the API endpoints.
"""

from fastapi.testclient import TestClient
from job_match_service.api import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_root_endpoint_with_message():
    response = client.get("/?message=test")
    assert response.status_code == 200
    assert response.json() == {"message": "test"}

def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"} 