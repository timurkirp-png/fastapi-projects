from pydantic import BaseModel, ConfigDict


class Task_schemas(BaseModel):
    id: str
    title: str
    completed: bool
    model_config = ConfigDict(from_attributes=True)


class Task_create_schemas(BaseModel):
    title: str


class Task_Update_schemas(BaseModel):
    title: str | None = None
    completed: bool | None = None


class Category(BaseModel):
    id: str
    name: str
    model_config = ConfigDict(from_attributes=True)


class Create_Category(BaseModel):
    name: str


class Update_Category(BaseModel):
    name: str | None = None
