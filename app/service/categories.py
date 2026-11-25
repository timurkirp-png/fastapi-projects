from sqlalchemy.orm import Session

from app.repository.categories import CategoryRepository
from app.schemas.schema import (
    Category,
    Create_Category,
    Update_Category,
)


class CategoryNotFound(Exception):
    """Задача не неайдена в БД"""


class CategoryService:
    def __init__(self, db: Session) -> None:
        self.db = db
        self.category_repository = CategoryRepository(db)

    def create_category(self, category_create: Create_Category) -> Category:
        category_orm = self.category_repository.create(name=category_create.name)
        self.db.commit()
        return category_orm

    def list_category(self) -> list[Category]:
        category_orm = self.category_repository.get_all()
        return [
            Category.model_validate(category, from_attributes=True)
            for category in category_orm
        ]

    def update_category(
        self, category_id: str, category_update: Update_Category
    ) -> Category:
        category_for_update = self.category_repository.get_by_id(
            category_id=category_id
        )
        if not category_for_update:
            raise CategoryNotFound(f"категория c id {category_id} не найдена")

        if category_update.name is not None:
            category_for_update.name = category_update.name
        self.db.commit()
        return Category.model_validate(category_for_update)

    def delete_category(self, category_id: str):
        category_for_delete = self.category_repository.get_by_id(
            category_id=category_id
        )
        if not category_for_delete:
            raise CategoryNotFound(f"категория c id {category_id} не найдена")
        self.category_repository.delete(category_for_delete)
        self.db.commit()
