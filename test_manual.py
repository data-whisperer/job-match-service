"""
Manual test script for the job-match-service API.
"""

import sys
import os
from pathlib import Path

# Add the src directory to the Python path
src_path = str(Path(__file__).parent)
sys.path.insert(0, src_path)

from fastapi.testclient import TestClient
from src.job_match_service.api import app

# Initialize the test client
client = TestClient(app=app)

def test_root_endpoint():
    response = client.get("/")
    print(f"Root endpoint status: {response.status_code}")
    print(f"Response: {response.json()}")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
    print("Root endpoint test passed!")

def test_health_endpoint():
    response = client.get("/health")
    print(f"Health endpoint status: {response.status_code}")
    print(f"Response: {response.json()}")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
    print("Health endpoint test passed!")

if __name__ == "__main__":
    print("Running manual tests...")
    test_root_endpoint()
    test_health_endpoint()
    print("All manual tests passed!") 