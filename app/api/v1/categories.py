from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status

from app.api.dependencies import get_category_service
from app.schemas.schema import (
    Category,
    Create_Category,
    Update_Category,
)
from app.service import categories as categories_service

# from app.repository import wallets as wallets_repository


router = APIRouter()


@router.get("/categories")
def read_category(
    category_service: Annotated[
        categories_service.CategoryService, Depends(get_category_service)
    ],
) -> list[Category]:
    return category_service.list_category()


@router.post("/categories", status_code=status.HTTP_201_CREATED)
def create_category(
    payload: Create_Category,
    category_service: Annotated[
        categories_service.CategoryService, Depends(get_category_service)
    ],
) -> Category:
    return category_service.create_category(category_create=payload)


@router.patch("/categories/{category_id}")
def update_task(
    category_id: str,
    payload: Update_Category,
    category_service: Annotated[
        categories_service.CategoryService, Depends(get_category_service)
    ],
) -> Category:
    try:
        return category_service.update_category(
            category_id=category_id, category_update=payload
        )
    except categories_service.CategoryNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.delete("/categories/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(
    category_id: str,
    category_service: Annotated[
        categories_service.CategoryService, Depends(get_category_service)
    ],
):
    try:
        return category_service.delete_category(category_id=category_id)
    except categories_service.CategoryNotFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
