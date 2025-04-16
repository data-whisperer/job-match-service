# Job Match Service

A microservice for text similarity comparison using AI embeddings.

## Features

- Single profile comparison
- Batch job profile comparison
- AI-powered text similarity using embeddings
- Input validation and error handling

## Requirements

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd job-match-service
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the package in development mode:
```bash
pip install -e ".[dev]"
```

## Running the Service

1. Start the service:
```bash
python src/main.py
```

The service will start on `http://localhost:8000`

## API Endpoints

### Single Profile Comparison
```bash
curl -X POST http://localhost:8000/compare-profiles \
  -H "Content-Type: application/json" \
  -d '{
    "user_profile": "Python developer with 5 years of experience",
    "job_profile": "Senior Python developer position"
  }'
```

### Batch Job Profile Comparison
```bash
curl -X POST http://localhost:8000/compare-profiles/batch \
  -H "Content-Type: application/json" \
  -d '{
    "user_profile": "Python developer with 5 years of experience",
    "job_profiles": [
      "Senior Python developer position",
      "Full-stack developer position",
      "Backend developer role"
    ]
  }'
```

## Development

### Running Tests
```bash
pytest
```

### Code Formatting
```bash
black src tests
isort src tests
```

## API Documentation

Once the service is running, you can access:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc
