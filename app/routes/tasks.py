from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.schemas.task import TaskCreate, TaskUpdate
from app.service.taks import create_task, delete_task, get_tasks, update_task
from app.utils.health_check import check_db_connection


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()    

router.post('task')
def create(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db, task)

router.get('task')
def get(limit: int = 10, offset: int = 0, db: Session = Depends(get_db)):
    return get_tasks(db, limit, offset)

router.put('task')
def update(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    return update_task(db, task_id, task)

router.delete('task')
def delete(task_id: int, db: Session = Depends(get_db)):
    return delete_task(db, task_id)

router.get('health_check')
def health_check():
    return {'databse': check_db_connection()}