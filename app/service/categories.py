from typing import Annotated

from fastapi import Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.DB.session import get_db
from app.models.categories import CategoryORM
from app.repository.categories import category_to_model
from app.schemas.schema import (
    Category,
    Create_Category,
    Update_Category,
)


def get_categories(db: Annotated[Session, Depends(get_db)]) -> list[Category]:
    categories_from_db = db.scalars(select(CategoryORM)).all()
    return [category_to_model(category) for category in categories_from_db]


def create_category(payload: Create_Category,db: Annotated[Session, Depends(get_db)]) -> Category:
    new_category = CategoryORM(name=payload.name)
    db.add(new_category)
    db.commit()
    return category_to_model(new_category)



def update_category(category_id: str, payload: Update_Category, db: Annotated[Session, Depends(get_db)]):
    category_for_update = db.get(CategoryORM, category_id)
    if category_for_update is None:
        raise HTTPException(status_code=404, detail="title is None")

    if payload.name is not None:
        category_for_update.name = payload.name
    
    db.commit()
    return category_to_model(category_for_update)



def delete_category(category_id, db: Annotated[Session, Depends(get_db)]):
    category_for_update = db.get(CategoryORM, category_id)
    if category_for_update is None:
        raise HTTPException(status_code=404, detail="title is None")
    db.delete(category_for_update)
    db.commit()
    return category_for_update