#!/bin/bash

# Test root endpoint
curl "http://localhost:8000/?message=test"

# Test POST compare-profiles endpoint
curl -X POST "http://localhost:8000/compare-profiles" \
-H "Content-Type: application/json" \
-d '{"user_profile": "Python developer with 5 years of experience", "job_profile": "Senior Python developer position"}'

# Test POST compare-profiles/batch endpoint
curl -X POST "http://localhost:8000/compare-profiles/batch" \
-H "Content-Type: application/json" \
-d '{"user_profile": "Python developer", "job_profiles": ["Senior Python developer position", "Backend developer role focusing on Python"]}'
