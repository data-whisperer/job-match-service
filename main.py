"""
Main entry point for the FastAPI application.

This script initializes the FastAPI app, and starts the server.
"""

from fastapi import FastAPI

app = FastAPI(title="API for job-match-service", version="0.1.0")

@app.get("/")
async def root(message: str = "Hello World"):
    return {"message": message}

@app.get("/health")
async def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
