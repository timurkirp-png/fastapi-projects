from pydantic import BaseModel


class Task_shemas(BaseModel):
    id: str
    title: str
    completed: bool


class Task_create_shemas(BaseModel):
    title: str

class Category_shemas(BaseModel):
    id: str
    Favorite_book: str 
    reading: bool
