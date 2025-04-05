import uuid
from sqlalchemy import Column, String, Enum, DateTime
from sqlalchemy.sql import func
from app.db.base import Base 
import enum

class TaskStatus(str, enum.Enum):
    pending = "pending"
    in_progress = "in-progress"
    completed = "completed"

class Task(Base):
    __tablename__ = "tasks"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    status = Column(Enum(TaskStatus), nullable=False, default=TaskStatus.pending)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), server_default=func.now())
