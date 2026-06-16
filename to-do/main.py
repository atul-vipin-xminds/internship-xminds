from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import Base, engine, get_db

from models import (
    User,
    Task,
    TaskDetail,
    Tag
)

from schemas import (
    UserCreate,
    UserResponse,
    TaskCreate,
    TaskResponse,
    TaskDetailCreate,
    TaskDetailResponse,
    TagCreate,
    TagResponse
)

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {
        "message": "Todo App API"
    }


#create user

@app.post(
    "/users",
    response_model=UserResponse
)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    db_user = User(
        name=user.name,
        email=user.email
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user


@app.get(
    "/users/{user_id}",
    response_model=UserResponse
)
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


#create task

@app.post(
    "/tasks",
    response_model=TaskResponse
)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db)
):
    user = db.query(User).filter(
        User.id == task.user_id
    ).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    

    db_task = Task(
        title=task.title,
        completed=task.completed,
        user_id=task.user_id
    )

    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task


@app.get(
    "/tasks/{task_id}",
    response_model=TaskResponse
)
def get_task(
    task_id: int,
    db: Session = Depends(get_db)
):
    task = db.query(Task).filter(
        Task.id == task_id
    ).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task


#create task_detail

@app.post(
    "/tasks/{task_id}/detail",
    response_model=TaskDetailResponse
)
def create_task_detail(
    task_id: int,
    detail: TaskDetailCreate,
    db: Session = Depends(get_db)
):
    task = db.query(Task).filter(
        Task.id == task_id
    ).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    db_detail = TaskDetail(
        description=detail.description,
        due_date=detail.due_date,
        task_id=task_id
    )

    db.add(db_detail)
    db.commit()
    db.refresh(db_detail)

    return db_detail


#create_tag

@app.post(
    "/tags",
    response_model=TagResponse
)
def create_tag(
    tag: TagCreate,
    db: Session = Depends(get_db)
):
    db_tag = Tag(
        tag_name=tag.tag_name
    )

    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)

    return db_tag


#assign_tag

@app.post("/tasks/{task_id}/tags/{tag_id}")
def assign_tag(
    task_id: int,
    tag_id: int,
    db: Session = Depends(get_db)
):
    task = db.query(Task).filter(
        Task.id == task_id
    ).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    tag = db.query(Tag).filter(
        Tag.id == tag_id
    ).first()

    if not tag:
        raise HTTPException(
            status_code=404,
            detail="Tag not found"
        )

    task.tags.append(tag)

    db.commit()

    return {
        "message": "Tag assigned successfully"
    }