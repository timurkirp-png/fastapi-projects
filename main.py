from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.categories import router as categories_router
from app.api.v1.tasks import router as tasks_router
from app.core.middleware import log_requests

# from lifespan import lifespan

# lifespan=lifespan

app = FastAPI()

app.middleware("http")(log_requests)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
)

app.include_router(categories_router, prefix="/app/api/v1", tags=["category"])

app.include_router(tasks_router, prefix="/app/api/v1", tags=["tasks"])


# git add .
# git commit -m "Что я сделал"
# git push
