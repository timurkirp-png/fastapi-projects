from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.task import TaskORM, task_to_model
from app.schemas.schema import Task_schemas


class TaskRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create(self, title: str) -> Task_schemas:
        new_task = TaskORM(title=title, completed=False)
        self.db.add(new_task)
        self.db.commit()
        return task_to_model(new_task)

    def get_all(self)-> list[TaskORM]:
        return list(self.db.scalars(select(TaskORM)).all())

    def get_by_id(self, task_id: str)-> TaskORM | None:
        return self.db.get(TaskORM, task_id)

    def delete(self, TaskORM) -> None:
        self.db.delete(TaskORM)
