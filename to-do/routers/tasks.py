from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from database import get_db

from models import (
    User,
    Task
)

from schemas import (
    TaskCreate,
    TaskResponse
)

from auth import (
    get_current_user,
    all_user_task_list
)

router = APIRouter()


@router.post(
    "/",
    response_model=TaskResponse
)
def create_task(
    task: TaskCreate,
    current_user: dict = Depends(
        get_current_user
    ),
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


@router.get(
    "/",
    response_model=list[TaskResponse]
)
def get_all_tasks(
    current_user: dict = Depends(
        all_user_task_list
    ),
    db: Session = Depends(get_db)
):
    return db.query(Task).all()


@router.get(
    "/{task_id}",
    response_model=TaskResponse
)
def get_task(
    task_id: int,
    current_user: dict = Depends(
        get_current_user
    ),
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