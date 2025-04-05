from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.schemas.task import TaskCreate, TaskOut, TaskUpdate
from app.service.task import create_task, delete_task, get_tasks, update_task
from app.utils.health_check import check_db_connection

router = APIRouter()


# Dependency for getting DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/task", response_model=TaskOut)
def create_task_route(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db, task)


@router.get("/task", response_model=List[TaskOut])
def get_tasks_route(limit: int = 10, offset: int = 0, db: Session = Depends(get_db)):
    return get_tasks(db, limit, offset)


@router.put("/task/{task_id}", response_model=TaskOut)
def update_task_route(task_id: str, task: TaskUpdate, db: Session = Depends(get_db)):
    updated = update_task(db, task_id, task)
    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated


@router.delete("/task/{task_id}", status_code=204)
def delete_task_route(task_id: str, db: Session = Depends(get_db)):
    deleted = delete_task(db, task_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")


@router.get("/health_check")
def health_check():
    return {"database": check_db_connection()}
