from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.DB.session import engine
from app.models.models_base import Base


@asynccontextmanager
async def lifespan( _: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield