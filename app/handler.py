from uuid import uuid4

from fastapi import APIRouter

from app.schema import Category_shemas, Task_create_shemas, Task_shemas

router = APIRouter()

book: list[Category_shemas] = []

tasks: list[Task_shemas] = []

@router.get("/tasks")
def read_tasks() -> list[Task_shemas]:
    return tasks

@router.post("/tasks")
def create_tasks(payload: Task_create_shemas) -> Task_shemas:
    new_tasks = Task_shemas(id=str(uuid4()), title=payload.title, completed=False)

    tasks.append(new_tasks)
    return new_tasks

@router.post("/categories")
def create_category(payload: Task_create_shemas) -> Category_shemas:
    new_category = Category_shemas(id=str(uuid4()), Favorite_book=payload.title, reading=False)
    book.append(new_category)
    return new_category

@router.get("/categories")
def read_category() -> list[Category_shemas]:
    return book

