"""
Main entry point for the job-match-service.
"""

import uvicorn
from job_match_service.api import app

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) 