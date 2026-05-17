# Task Manager API

A full-stack Task Manager application built using FastAPI, SQLite, HTML, CSS, and JavaScript.

The project allows users to create, view, update, complete, and delete tasks through RESTful API endpoints and a simple frontend interface.

---

## Features

- Create new tasks
- View all tasks
- Update task details
- Mark tasks as completed/pending
- Delete tasks
- SQLite database integration
- REST API architecture
- Pydantic request validation
- Interactive Swagger API documentation
- Frontend integration using JavaScript fetch API

---

## Tech Stack

### Backend
- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

### Frontend
- HTML
- CSS
- Vanilla JavaScript

---

## Project Structure

```text
task-manager-api/
│
├── main.py
├── database.py
├── models.py
├── schemas.py
├── requirements.txt
│
├── static/
│   ├── style.css
│   └── script.js
│
└── templates/
    └── index.html
```

---

## Installation & Setup

### 1. Clone Repository

```bash
git clone <your-github-repo-link>
cd task-manager-api
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run Application

```bash
uvicorn main:app --reload
```

---

## API Documentation

Swagger UI available at:

```text
http://127.0.0.1:8000/docs
```

Frontend available at:

```text
http://127.0.0.1:8000/home
```

---

## Future Improvements

- User authentication
- Task deadlines and priorities
- Cloud deployment
- Pagination support
- Docker containerization

---

## Author

Harshit Goel