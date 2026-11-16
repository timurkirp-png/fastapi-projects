from typing import Annotated

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.DB.session import get_db
from app.schemas.schema import (
    Category,
    Create_Category,
    Update_Category,
)
from app.service import categories as categories_service

# from app.repository import wallets as wallets_repository


router = APIRouter()

@router.get("/categories")
def get_category(db: Annotated[Session, Depends(get_db)]) -> list[Category]:
    return categories_service.get_categories(db)

@router.post("/categories", status_code=status.HTTP_201_CREATED)
def create_category(payload: Create_Category,db: Annotated[Session, Depends(get_db)]) -> Category:
    return categories_service.create_category(payload, db)

@router.patch("/categories/{category_id}")
def update_category(category_id: str, payload: Update_Category, db: Annotated[Session, Depends(get_db)]):
    return categories_service.update_category(category_id, payload, db)

@router.delete("/categories/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id, db: Annotated[Session, Depends(get_db)]):
        return categories_service.delete_category(category_id, db)