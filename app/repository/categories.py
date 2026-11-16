from app.models.categories import CategoryORM
from app.schemas.schema import Category


def category_to_model(category_orm: CategoryORM) -> Category:
    return Category(id=category_orm.id, name=category_orm.name)