"""
FastAPI application setup and route definitions.
"""

from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, validator
from .embeddings import EmbeddingService
from .similarity import SimilarityService
from .config import settings

app = FastAPI(title="API for job-match-service", version=settings.api_version)

# Initialize services
embedding_service = EmbeddingService(model_name=settings.embedding_model)
similarity_service = SimilarityService()

class ProfileComparisonRequest(BaseModel):
    user_profile: str = Field(..., min_length=1, max_length=10000)
    job_profile: str = Field(..., min_length=1, max_length=10000)

    @validator('user_profile', 'job_profile')
    def validate_profile(cls, v):
        if not v.strip():
            raise ValueError('Profile cannot be empty or whitespace')
        return v.strip()

class ProfileComparisonResponse(BaseModel):
    similarity_score: float = Field(..., ge=0, le=1)

class BatchJobProfileRequest(BaseModel):
    user_profile: str = Field(..., min_length=1, max_length=10000)
    job_profiles: List[str] = Field(..., min_items=1, max_items=100)

    @validator('user_profile')
    def validate_user_profile(cls, v):
        if not v.strip():
            raise ValueError('User profile cannot be empty or whitespace')
        return v.strip()

    @validator('job_profiles')
    def validate_job_profiles(cls, v):
        if not all(profile.strip() for profile in v):
            raise ValueError('Job profiles cannot be empty or whitespace')
        return [profile.strip() for profile in v]

class BatchJobProfileResponse(BaseModel):
    similarity_scores: List[float] = Field(..., min_items=1)

@app.get("/")
async def root(message: str = "Hello World"):
    return {"message": message}

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/compare-profiles", response_model=ProfileComparisonResponse)
async def compare_profiles(request: ProfileComparisonRequest):
    try:
        # Generate embeddings for both profiles
        user_embedding = embedding_service.get_embedding(request.user_profile)
        job_embedding = embedding_service.get_embedding(request.job_profile)
        
        # Calculate similarity
        similarity_score = similarity_service.calculate_similarity(
            user_embedding,
            job_embedding
        )
        
        return ProfileComparisonResponse(similarity_score=similarity_score)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing profiles: {str(e)}"
        )

@app.post("/compare-profiles/batch", response_model=BatchJobProfileResponse)
async def compare_profiles_batch(request: BatchJobProfileRequest):
    try:
        # Generate embedding for user profile (only once)
        user_embedding = embedding_service.get_embedding(request.user_profile)
        
        # Generate embeddings for all job profiles
        job_embeddings = embedding_service.get_embeddings(request.job_profiles)
        
        # Calculate similarities
        similarity_scores = [
            similarity_service.calculate_similarity(user_embedding, job_emb)
            for job_emb in job_embeddings
        ]
        
        return BatchJobProfileResponse(similarity_scores=similarity_scores)
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error processing batch profiles: {str(e)}"
        ) 