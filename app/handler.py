from fastapi import APIRouter

from app.schema import TaskStatus, Title

router = APIRouter()

Title_lst = []

@router.get("/title", response_model=Title)
def create_title(id: int, title: str, status: TaskStatus):
    Title_lst.append(title)
    return {"title": title, "id": id, "status": status}


@router.get("/title,")
def get_all_title(Title_lst):
    return Title_lst