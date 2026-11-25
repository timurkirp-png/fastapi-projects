from sqlalchemy.orm import Session

from app.repository.tasks import TaskRepository
from app.schemas.schema import (
    Task_create_schemas,
    Task_schemas,
    Task_Update_schemas,
)


class TaskNotFound(Exception):
    """Задача не неайдена в БД"""


class TaskService:
    def __init__(self, db: Session) -> None:
        self.db = db
        self.task_repository = TaskRepository(db)

    def create_tasks(self, task_create: Task_create_schemas) -> Task_schemas:
        task_orm = self.task_repository.create(title=task_create.title)
        self.db.commit()
        return task_orm

    def list_tasks(self) -> list[Task_schemas]:
        task_orm = self.task_repository.get_all()
        return [
            Task_schemas.model_validate(task, from_attributes=True) for task in task_orm
        ]

    def update_tasks(
        self, task_id: str, task_update: Task_Update_schemas
    ) -> Task_schemas:
        tasks_for_update = self.task_repository.get_by_id(task_id=task_id)
        if not tasks_for_update:
            raise TaskNotFound(f"задача c id {task_id} не найдена")
        if task_update.title is not None:
            tasks_for_update.title = task_update.title
        if task_update.completed is not None:
            tasks_for_update.completed = task_update.completed

        self.db.commit()
        return Task_schemas.model_validate(tasks_for_update)

    def delete_tasks(self, task_id: str):
        tasks_for_delete = self.task_repository.get_by_id(task_id=task_id)
        if not tasks_for_delete:
            raise TaskNotFound(f"задача c id {task_id} не найдена")
        self.task_repository.delete(tasks_for_delete)
        self.db.commit()
