from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class TaskBase(BaseModel):
    name: str
    description: Optional[str] = None
    tag: Optional[str] = None

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    task_id: str
    created_time: Optional[str] = None
    updated_time: Optional[str] = None

    class Config:
        orm_mode = True
        fields = {
            'created_time': {'default_factory': lambda: str(datetime.utcnow())},
            'updated_time': {'default_factory': lambda: str(datetime.utcnow())},
        }


class TaskUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    tag: Optional[str] = None