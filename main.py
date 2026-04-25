from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Task Manager API")

# In-memory storage for now (replace with SQLite later)
tasks = []
task_counter = 1

class Task(BaseModel):
    title: str
    description: str = ""
    completed: bool = False

class TaskResponse(Task):
    id: int

@app.get("/")
def read_root():
    return {"message": "Welcome to Task Manager API", "docs": "/docs"}

@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks():
    return tasks

@app.post("/tasks", response_model=TaskResponse, status_code=201)
def create_task(task: Task):
    global task_counter
    new_task = {"id": task_counter, **task.dict()}
    tasks.append(new_task)
    task_counter += 1
    return new_task

@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    global tasks
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(i)
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")