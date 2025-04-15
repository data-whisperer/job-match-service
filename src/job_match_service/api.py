"""
FastAPI application setup and route definitions.
"""

from fastapi import FastAPI

app = FastAPI(title="API for job-match-service", version="0.1.0")

@app.get("/")
async def root(message: str = "Hello World"):
    return {"message": message}

@app.get("/health")
async def health():
    return {"status": "ok"} 