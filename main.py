
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.handler import router as handler_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"], 
    )

app.include_router(handler_router, prefix="", tags=["title"])
