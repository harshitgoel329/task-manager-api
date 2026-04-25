# Task Manager API

A RESTful API for managing tasks, built with FastAPI and SQLite.

## Tech Stack
- Python
- FastAPI
- SQLite (upcoming)
- Pydantic

## Features
- Create, read, and delete tasks
- Input validation with Pydantic
- Auto-generated API documentation at `/docs`

## Run Locally
```bash
pip install -r requirements.txt
uvicorn main:app --reload