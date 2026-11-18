
from sqlalchemy.orm import Mapped, mapped_column

from app.models.models_base import Base
from app.schemas.schema import Task_schemas


class TaskORM(Base):
    __tablename__ = "tasks"

    title: Mapped[str]
    completed: Mapped[bool] = mapped_column(default=False)

def task_to_model(task_orm: TaskORM) -> Task_schemas:
    return Task_schemas(id=task_orm.id, title=task_orm.title, completed=task_orm.completed)




