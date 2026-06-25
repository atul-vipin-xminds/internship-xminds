import logging
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from auth import admin_required, user_required
from database import get_db
from models import User, PointHistory
from schemas import PointHistoryResponse

router = APIRouter()


@router.get("/my-history", response_model=list[PointHistoryResponse])
async def my_point_history(
    current_user: dict = Depends(user_required), db: AsyncSession = Depends(get_db)
):
    try:
        result = await db.execute(
            select(User).where(User.username == current_user["sub"])
        )
        user = result.scalar_one_or_none()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        result = await db.execute(
            select(PointHistory).where(PointHistory.user_id == user.id)
        )
        history = result.scalars().all()
        return history
    except HTTPException:
        raise
    except Exception:
        logging.error("Unable to fetch point history", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/user/{user_id}", response_model=list[PointHistoryResponse])
async def get_user_point_history(
    user_id: str,
    current_user: dict = Depends(admin_required),
    db: AsyncSession = Depends(get_db),
):
    try:
        result = await db.execute(select(User).where(User.id == user_id))
        user = result.scalar_one_or_none()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        result = await db.execute(
            select(PointHistory).where(PointHistory.user_id == user_id)
        )
        history = result.scalars().all()
        return history
    except HTTPException:
        raise
    except Exception:
        logging.error("Unable to fetch user point history", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/", response_model=list[PointHistoryResponse])
async def get_all_point_history(
    current_user: dict = Depends(admin_required), db: AsyncSession = Depends(get_db)
):
    try:
        result = await db.execute(select(PointHistory))
        history = result.scalars().all()
        return history
    except Exception:
        logging.error("Unable to fetch all point history", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")
