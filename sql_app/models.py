from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .database import Base
import uuid
from datetime import datetime


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    tag = Column(String)
    task_id = Column(String, unique=True, index=True, default=str(uuid.uuid4()))
    created_time = Column(String, default=str(datetime.utcnow()))
    updated_time = Column(String, default=str(datetime.utcnow()), onupdate=str(datetime.utcnow()))