from fastapi import FastAPI

from database import Base, engine

from routers import (
    users,
    tasks,
    task_details,
    tags
)

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {
        "message": "Todo App API"
    }


app.include_router(
    users.router,
    prefix="/users",
    tags=["Users"]
)

app.include_router(
    tasks.router,
    prefix="/tasks",
    tags=["Tasks"]
)

app.include_router(
    task_details.router,
    prefix="/tasks",
    tags=["Task Details"]
)

app.include_router(
    tags.router,
    tags=["Tags"]
)