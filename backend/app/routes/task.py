from typing import List
from fastapi import APIRouter, Depends  # Body,
from sqlalchemy.orm import Session
from app import models, utils, schemas

router = APIRouter()

@router.get("/tasks", response_model=List[models.Task])
def get_tasks(*, db: Session = Depends(utils.get_db)):
    tasks = db.query(schemas.Task).all()
    return tasks
    
@router.get("/task", response_model=models.Task)
def get_task(*, db: Session = Depends(utils.get_db), id: int):
    task = db.query(schemas.Task).filter(schemas.Task.id == id).first()
    return task

@router.post("/task", response_model=models.Task)
def create_task(*, db: Session = Depends(utils.get_db), task: models.Task):
    task_data = task.dict(exclude_unset=True)
    db_task = schemas.Task(**task_data)
    db.add(db_task)
    db.commit()
    return db_task

@router.patch("/task", response_model=models.Task)
def edit_task(*, db: Session = Depends(utils.get_db), task: models.Task):
    db_task = db.query(schemas.Task).filter(schemas.Task.id == task.id).first()
    task_data = task.dict(exclude_unset=True)
    for key, value in task_data.items():
        setattr(db_task, key, value)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@router.delete("/task")
def delete_task(*, db: Session = Depends(utils.get_db), id: int):
    db.query(schemas.Task).filter(schemas.Task.id == id).delete()
    db.commit()