from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create
@app.post("/tasks", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = crud.create_task(db=db, task=task)
    return db_task

# Read all tasks and fillter tasks by tag
# make tag param optional so user can filter by tag or not
@app.get("/tasks/", response_model=list[schemas.Task])
def read_tasks(tag: str = None, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    if tag:
        tasks = db.query(models.Task).filter(models.Task.tag.like(f"%{tag}%")).offset(skip).limit(limit).all()
    else:
        tasks = db.query(models.Task).offset(skip).limit(limit).all()
    return tasks  

@app.get("/tasks/name/{name}")
def read_tasks_by_name(name: str, db: Session = Depends(get_db)):
    tasks = crud.get_tasks_by_name(db, name)
    if not tasks:
        raise HTTPException(status_code=404, detail="Tasks not found")
    return tasks
    
# Update
@app.put("/tasks/{id}", response_model=schemas.Task)
def update_task(id: str, task: schemas.TaskUpdate, db: Session = Depends(get_db)):
    db_task = crud.get_task(db, id=id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    db_task = crud.update_task(db, id=id, task=task)
    return db_task


# Delete
@app.delete("/tasks/{id}")
def delete_task(id: str, db: Session = Depends(get_db)):
    task = crud.get_task(db, id=id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    crud.delete_task(db, id=id)
    return {"message": "Task deleted successfully"}