from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.categories import CategoryORM, category_to_model
from app.schemas.schema import Category


class CategoryRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create(self, name: str) -> Category:
        new_category = CategoryORM(name=name)
        self.db.add(new_category)
        self.db.commit()
        return category_to_model(new_category)

    def get_all(self) -> list[CategoryORM]:
        return list(self.db.scalars(select(CategoryORM)).all())

    def get_by_id(self, category_id: str) -> CategoryORM | None:
        return self.db.get(CategoryORM, category_id)

    def delete(self, CategoryORM) -> None:
        self.db.delete(CategoryORM)
