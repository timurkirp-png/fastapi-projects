from uuid import uuid4

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker

from app.schema import Category, Task_schemas

DATABASE_URL = "postgresql+psycopg://postgres:admin@127.0.0.1:15432/postgres"

engine = create_engine(DATABASE_URL)

Session_local = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    id: Mapped[str] = mapped_column(primary_key=True, default=lambda: str(uuid4()))


class TaskORM(Base):
    __tablename__ = "tasks"

    title: Mapped[str]
    completed: Mapped[bool] = mapped_column(default=False)

class CategoryORM(Base):
    __tablename__ = "categories"
    name: Mapped[str]

def get_db():
    db = Session_local()
    try:
        yield db
    finally:
        db.close()

def task_to_model(task_orm: TaskORM) -> Task_schemas:
    return Task_schemas(id=task_orm.id, title=task_orm.title, completed=task_orm.completed)

def category_to_model(category_orm: CategoryORM) -> Category:
    return Category(id=category_orm.id, name=category_orm.name)