from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Task, TaskDetail
from schemas import (
    TaskDetailCreate,
    TaskDetailResponse
)

router = APIRouter()


@router.post(
    "/{task_id}/detail",
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