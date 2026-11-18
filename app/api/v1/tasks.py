from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from app.api.dependencies import get_tasks_service
from app.schemas.schema import (
    Task_create_schemas,
    Task_schemas,
    Task_Update_schemas,
)
from app.service import tasks as tasks_service

router = APIRouter()

@router.get("/tasks")
def read_tasks(task_service: Annotated[tasks_service.TaskService, Depends(get_tasks_service)]) -> list[Task_schemas]:
    return task_service.list_tasks()

@router.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_tasks(payload: Task_create_schemas, task_service: Annotated[tasks_service.TaskService, Depends(get_tasks_service)]) -> Task_schemas:
    return task_service.create_tasks(task_create=payload)

@router.patch("/tasks/{task_id}")
def update_task(task_id: str, payload: Task_Update_schemas, task_service: Annotated[tasks_service.TaskService, Depends(get_tasks_service)]) -> Task_schemas:
    try:
        return task_service.update_tasks(task_id=task_id, task_update=payload)
    except tasks_service.TaskNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@router.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id, task_service: Annotated[tasks_service.TaskService, Depends(get_tasks_service)]):
    try:
        return task_service.delete_tasks(task_id=task_id)
    except tasks_service.TaskNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)