from sqlalchemy.orm import Mapped

from app.api.dependencies import get_category_service
from app.models.models_base import Base
from app.schemas.schema import Category


class CategoryORM(Base):
    __tablename__ = "categories"
    name: Mapped[str]


def category_to_model(category_orm: CategoryORM) -> Category:
    return Category(id=category_orm.id, name=category_orm.name)
