"""
Script to run the service and test it manually.
"""

import subprocess
import time
import requests
import sys
import os
from pathlib import Path

# Add the src directory to the Python path
src_path = str(Path(__file__).parent)
sys.path.insert(0, src_path)

def run_service():
    """Run the service in a separate process."""
    print("Starting the service...")
    process = subprocess.Popen(
        ["python", "src/main.py"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    return process

def test_endpoints():
    """Test the API endpoints."""
    print("\nTesting endpoints...")
    
    # Test root endpoint
    try:
        response = requests.get("http://localhost:8000/")
        print(f"Root endpoint status: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Error testing root endpoint: {e}")
    
    # Test health endpoint
    try:
        response = requests.get("http://localhost:8000/health")
        print(f"Health endpoint status: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Error testing health endpoint: {e}")
    
    # Test compare-profiles endpoint
    try:
        test_data = {
            "user_profile": "Python developer with 5 years of experience",
            "job_profile": "Senior Python developer position"
        }
        response = requests.post(
            "http://localhost:8000/compare-profiles",
            json=test_data
        )
        print(f"Compare profiles endpoint status: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Error testing compare-profiles endpoint: {e}")

if __name__ == "__main__":
    # Run the service
    process = run_service()
    
    # Wait for the service to start
    print("Waiting for the service to start...")
    time.sleep(3)
    
    try:
        # Test the endpoints
        test_endpoints()
    finally:
        # Terminate the service
        print("\nTerminating the service...")
        process.terminate()
        process.wait()
        print("Service terminated.") 