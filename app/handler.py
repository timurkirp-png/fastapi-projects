from uuid import uuid4

from fastapi import APIRouter, HTTPException, status

from app.schema import (
    Category,
    Create_Category,
    Task_create_schemas,
    Task_schemas,
    Update_Category,
    Update_schemas,
)

router = APIRouter()

categories: list[Category] = []

tasks: list[Task_schemas] = []

@router.get("/tasks")
def read_tasks() -> list[Task_schemas]:
    return tasks

@router.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_tasks(payload: Task_create_schemas) -> Task_schemas:
    new_tasks = Task_schemas(id=str(uuid4()), title=payload.title, completed=False)
    tasks.append(new_tasks)
    return new_tasks

@router.patch("/tasks/{task_id}")
def update_task(task_id: str, payload: Update_schemas):
    for task in tasks:
        if task.id == task_id:
            if payload.title is not None:
                task.title = payload.title
            if payload.completed is not None:
                task.completed = payload.completed
            return task


@router.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)


@router.get("/categories")
def get_category() -> list[Category]:
    return categories


@router.post("/categories", status_code=status.HTTP_201_CREATED)
def create_category(payload: Create_Category) -> Category:
    new_category = Category(id=str(uuid4()), name=payload.name)
    categories.append(new_category)
    return new_category

@router.patch("/categories/{category_id}")
def update_category(category_id: str, payload: Update_Category):
    for category in categories:
        if category.id == category_id and payload.name is not None:
            category.name = payload.name
        return category
    raise HTTPException(status_code=404, detail="Category not found")

@router.delete("/categories/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id):
    for category in categories:
        if category.id == category_id:
            categories.remove(category)
    raise HTTPException(status_code=404, detail="Category not found")
