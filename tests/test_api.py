"""
Tests for the API endpoints.
"""

from fastapi.testclient import TestClient
from job_match_service.api import app

# Initialize the test client correctly
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

def test_compare_profiles():
    test_data = {
        "user_profile": "Python developer with 5 years of experience in web development",
        "job_profile": "Senior Python developer position requiring web development skills"
    }
    response = client.post("/compare-profiles", json=test_data)
    assert response.status_code == 200
    assert "similarity_score" in response.json()
    assert 0 <= response.json()["similarity_score"] <= 1

def test_compare_profiles_validation():
    # Test empty profile
    test_data = {
        "user_profile": "",
        "job_profile": "Some job profile"
    }
    response = client.post("/compare-profiles", json=test_data)
    assert response.status_code == 422

    # Test whitespace profile
    test_data = {
        "user_profile": "   ",
        "job_profile": "Some job profile"
    }
    response = client.post("/compare-profiles", json=test_data)
    assert response.status_code == 422

    # Test too long profile
    test_data = {
        "user_profile": "a" * 10001,
        "job_profile": "Some job profile"
    }
    response = client.post("/compare-profiles", json=test_data)
    assert response.status_code == 422

def test_compare_profiles_batch():
    test_data = {
        "user_profile": "Python developer with 5 years of experience in web development",
        "job_profiles": [
            "Senior Python developer position requiring web development skills",
            "Full-stack developer position with Python experience",
            "Backend developer role focusing on Python and APIs"
        ]
    }
    response = client.post("/compare-profiles/batch", json=test_data)
    assert response.status_code == 200
    assert "similarity_scores" in response.json()
    assert len(response.json()["similarity_scores"]) == 3
    assert all(0 <= score <= 1 for score in response.json()["similarity_scores"])

def test_compare_profiles_batch_validation():
    # Test empty user profile
    test_data = {
        "user_profile": "",
        "job_profiles": ["Some job profile"]
    }
    response = client.post("/compare-profiles/batch", json=test_data)
    assert response.status_code == 422

    # Test empty job profiles list
    test_data = {
        "user_profile": "Some user profile",
        "job_profiles": []
    }
    response = client.post("/compare-profiles/batch", json=test_data)
    assert response.status_code == 422

    # Test too many job profiles
    test_data = {
        "user_profile": "Some user profile",
        "job_profiles": ["Job profile"] * 101
    }
    response = client.post("/compare-profiles/batch", json=test_data)
    assert response.status_code == 422

    # Test empty job profile in list
    test_data = {
        "user_profile": "Some user profile",
        "job_profiles": ["Job profile", "", "Another job profile"]
    }
    response = client.post("/compare-profiles/batch", json=test_data)
    assert response.status_code == 422 