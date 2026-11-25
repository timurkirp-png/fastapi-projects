# app/api/v1/router.py
from fastapi import APIRouter, Depends

from app.api.dependencies import get_category_service, get_tasks_service
from app.api.v1.categories import router as category_router
from app.api.v1.tasks import router as tasks_router

api_router = APIRouter(
    prefix="/api/v1",
    dependencies=[
        Depends(get_category_service),
        Depends(get_tasks_service),
    ],  # ← применяется ко всем роутерам ниже
)

api_router.include_router(tasks_router, prefix="/tasks", tags=["tasks"])
api_router.include_router(category_router, prefix="/categories", tags=["categories"])
