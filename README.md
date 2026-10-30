# FastAPI Student CRUD API

A beginner-friendly REST API built using Python, FastAPI, and Pydantic.

## Features
- Create a student
- Get all students
- Get a student by ID
- Update student details
- Delete a student
- Error handling using HTTPException
- JWT authentication (planned)

## Technologies
- Python
- FastAPI
- Pydantic

## Run the Project

```bash
uv run uvicorn student_api:app --reload
```

Open http://127.0.0.1:8000/docs to test the API.

## Note
Student records are stored in memory and reset when the server restarts. 