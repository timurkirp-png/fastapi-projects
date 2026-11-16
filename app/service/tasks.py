from typing import Annotated

from fastapi import Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.DB.session import get_db
from app.models.task import TaskORM
from app.repository.tasks import task_to_model
from app.schemas.schema import (
    Task_create_schemas,
    Task_schemas,
    Task_Update_schemas,
)


def read_tasks(db: Annotated[Session, Depends(get_db)]) -> list[Task_schemas]:
    tasks_from_db = db.scalars(select(TaskORM)).all()
    return [task_to_model(task) for task in tasks_from_db]


def create_tasks(payload: Task_create_schemas, db: Annotated[Session, Depends(get_db)]) -> Task_schemas:
    new_tasks = TaskORM(title=payload.title, completed=False)
    db.add(new_tasks)
    db.commit()
    return task_to_model(new_tasks)



def update_task(task_id: str, payload: Task_Update_schemas, db: Annotated[Session, Depends(get_db)]) -> Task_schemas:
    tasks_for_update = db.get(TaskORM, task_id)
    if tasks_for_update is None:
        raise HTTPException(status_code=404, detail="title is None")

    if payload.title is not None:
        tasks_for_update.title = payload.title
    if payload.completed is not None:
        tasks_for_update.completed = payload.completed
    
    db.commit()
    return task_to_model(tasks_for_update)
    


def delete_task(task_id, db: Annotated[Session, Depends(get_db)]):
    tasks_for_update = db.get(TaskORM, task_id)
    db.delete(tasks_for_update)
    db.commit()
    return tasks_for_update