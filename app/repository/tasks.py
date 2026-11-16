from app.models.task import TaskORM
from app.schemas.schema import Task_schemas


def task_to_model(task_orm: TaskORM) -> Task_schemas:
    return Task_schemas(id=task_orm.id, title=task_orm.title, completed=task_orm.completed)