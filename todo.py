from datetime import datetime
from uuid import UUID
from fastapi import FastAPI, HTTPException

from pydantic import BaseModel

app = FastAPI()

todos = []

class Task(BaseModel):
  name: str
  description: str
  tag: str
  created_time: str
  updated_time: str
  task_id: UUID

@app.get("/")
def root():
  return {"Welcome to your To Do list"}

@app.get("/todos")
def read_todos():
  return todos

@app.get("/todos/{id}")
def read_task(id: int):
  return{"task": todos[id]}

@app.post("/todos/")
def create_task(task: Task):
  task.created_time = datetime.now()
  todos.append(task)
  return task

@app.put("/todos/{id}")
def update_task(id: int, task: Task):
  itemToUpdate = todos[id]
  itemToUpdate.name = task.name
  itemToUpdate.description = task.description
  itemToUpdate.updated_time = datetime.now()
  todos[id] = itemToUpdate
  return itemToUpdate

# delete 
@app.delete("/todos/{id}")
def delete_task(id: int):
  todos.pop(id)
  return todos

# search/filter on the todos - tag match 
@app.get("/todos/")
def filter_by_tag(tag: str):
  filtered_tasks = []
  for todo in todos:
    if todo.tag == tag:
      filtered_tasks.append(todo)
    
  if len(filtered_tasks) == 0:
    raise HTTPException(status_code=404, detail="Item not found")
  else:
    return filtered_tasks