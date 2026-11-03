from enum import Enum

from pydantic import BaseModel


class TaskStatus(str, Enum):
    COMPLETE = "completed"
    NOT_COMPLETE = "not completed"

class Title(BaseModel):
    id: int
    title: str
    status: TaskStatus = TaskStatus.NOT_COMPLETE