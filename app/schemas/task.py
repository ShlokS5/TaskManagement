from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from enum import Enum

class TaskStatus(str, Enum):
    pending = "pending"
    in_progress = "in-progress"
    completed = "completed"

class TaskBase(BaseModel):
    title: str
    description: Optional[str]

class TaskCreate(TaskBase):
    status: TaskStatus

class TaskUpdate(BaseModel):
    title: Optional[str]
    status: Optional[TaskStatus]

class TaskOut(TaskBase):
    id: str
    status: TaskStatus
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
