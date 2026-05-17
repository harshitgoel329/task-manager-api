from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

import models
import schemas
from database import engine, SessionLocal

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.responses import HTMLResponse

app = FastAPI(title="Task Manager API")

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# # Root endpoint
# @app.get("/")
# def read_root():
#     return {
#         "message": "Welcome to Task Manager API",
#         "docs": "/docs"
#     }
@app.get("/")
@app.get("/home", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )
# Create task
@app.post("/tasks", response_model=schemas.TaskResponse, status_code=201)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    
    new_task = models.TaskDB(
        title=task.title,
        description=task.description,
        completed=task.completed
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

# Get all tasks
@app.get("/tasks", response_model=list[schemas.TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    
    tasks = db.query(models.TaskDB).all()
    return tasks

# Get single task
@app.get("/tasks/{task_id}", response_model=schemas.TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    
    task = db.query(models.TaskDB).filter(models.TaskDB.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task

# Update task
@app.put("/tasks/{task_id}", response_model=schemas.TaskResponse)
def update_task(
    task_id: int,
    updated_task: schemas.TaskCreate,
    db: Session = Depends(get_db)
):
    
    task = db.query(models.TaskDB).filter(models.TaskDB.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task.title = updated_task.title
    task.description = updated_task.description
    task.completed = updated_task.completed

    db.commit()
    db.refresh(task)

    return task

# Delete task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    
    task = db.query(models.TaskDB).filter(models.TaskDB.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    db.delete(task)
    db.commit()

    return {"message": "Task deleted successfully"}