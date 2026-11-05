from pydantic import BaseModel


class Task_shemas(BaseModel):
    id: str
    title: str
    completed: bool


class Task_create_shemas(BaseModel):
    title: str

class Book_shemas(BaseModel):
    book: str 


class Favorite_book_schema(BaseModel):
    Favorite_book: str

