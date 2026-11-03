from fastapi import FastAPI

from app.handler import router as handler_router

app = FastAPI()

app.include_router(handler_router, prefix="/app", tags=["title"])
