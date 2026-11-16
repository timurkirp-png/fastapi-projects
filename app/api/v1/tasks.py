from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.DB.session import get_db
from app.schemas.schema import (
    Task_create_schemas,
    Task_schemas,
    Task_Update_schemas,
)
from app.service import tasks as tasks_service

router = APIRouter()

@router.get("/tasks")
def read_tasks(db: Annotated[Session, Depends(get_db)]) -> list[Task_schemas]:
    return tasks_service.read_tasks(db)

@router.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_tasks(payload: Task_create_schemas, db: Annotated[Session, Depends(get_db)]) -> Task_schemas:
    return tasks_service.create_tasks(payload, db)

@router.patch("/tasks/{task_id}")
def update_task(task_id: str, payload: Task_Update_schemas, db: Annotated[Session, Depends(get_db)]) -> Task_schemas:
    return tasks_service.update_task(task_id, payload, db)

@router.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id, db: Annotated[Session, Depends(get_db)]):
    return tasks_service.delete_task(task_id, db)