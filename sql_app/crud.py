from sqlalchemy.orm import Session

from . import models, schemas


def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(name=task.name, description=task.description, tag=task.tag)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_task(db: Session, id: str):
    return db.query(models.Task).filter(models.Task.id == id).first()


def get_tasks_by_name(db: Session, name: str):
    return db.query(models.Task).filter(models.Task.name == name).all()

def update_task(db: Session, id: str, task: schemas.TaskUpdate):
    db_task = db.query(models.Task).filter(models.Task.id == id).first()
    if db_task:
        for field, value in task.dict(exclude_unset=True, exclude={"created_time"}).items():
            setattr(db_task, field, value)
        db.commit()
        db.refresh(db_task)
        return db_task
    return None

def get_task_by_tag(db: Session, tag: str):
    return db.query(models.Task).filter(models.Task.tag == tag).first()

def delete_task(db: Session, id: str):
    task = db.query(models.Task).filter(models.Task.id == id).first()
    if task:
        db.delete(task)
        db.commit()
        return True
    return False