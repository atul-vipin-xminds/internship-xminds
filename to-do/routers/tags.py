from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from models import Task, Tag
from schemas import TagCreate, TagResponse

router = APIRouter()


@router.post(
    "/",
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


@router.post("/{task_id}/tags/{tag_id}")
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