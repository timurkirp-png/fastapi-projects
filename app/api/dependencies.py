
from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.DB.session import get_db
from app.service.categories import CategoryService
from app.service.tasks import TaskService


def get_tasks_service(db: Annotated[Session, Depends(get_db)]):
    # функция для иньекции зависимости TaskService
    return TaskService(db)

def get_category_service(db: Annotated[Session, Depends(get_db)]):
    # функция для иньекции зависимости TaskService
    return CategoryService(db)