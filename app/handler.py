from uuid import uuid4

from fastapi import APIRouter

from app.schema import (
    Book_shemas,
    Favorite_book_schema,
    Task_create_shemas,
    Task_shemas,
)

router = APIRouter()

book: list[Favorite_book_schema] = []

tasks: list[Task_shemas] = []

@router.get("/tasks")
def read_tasks() -> list[Task_shemas]:
    return tasks

@router.post("/tasks")
def create_tasks(payload: Task_create_shemas) -> Task_shemas:
    new_tasks = Task_shemas(id=str(uuid4()), title=payload.title, completed=False)

    tasks.append(new_tasks)
    return new_tasks

@router.post("/book")
def create_category(payload: Book_shemas) -> Favorite_book_schema:
    new_category = Favorite_book_schema(Favorite_book=payload.book)
    book.append(new_category)
    return new_category

@router.get("/book")
def read_category()-> list[Favorite_book_schema]:
    return book

