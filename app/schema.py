from pydantic import BaseModel


class Task_schemas(BaseModel):
    id: str
    title: str
    completed: bool


class Task_create_schemas(BaseModel):
    title: str

class Update_schemas(BaseModel):
    title: str | None = None
    completed: bool | None = None


class Category(BaseModel):
    id: str
    name: str

class Create_Category(BaseModel):
    name: str 

class Update_Category(BaseModel):
    name: str | None = None
    detail: str | None = "Category not found"

