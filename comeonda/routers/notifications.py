import logging
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from auth import admin_required, user_required
from database import get_db
from models import User, Notification
from schemas import NotificationResponse

router = APIRouter()


@router.get("/my-notifications", response_model=list[NotificationResponse])
async def my_notifications(
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
            select(Notification).where(Notification.user_id == user.id)
        )
        notifications = result.scalars().all()
        return notifications
    except HTTPException:
        raise
    except Exception:
        logging.error("Unable to fetch notifications", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.patch("/{notification_id}/read", response_model=NotificationResponse)
async def mark_as_read(
    notification_id: str,
    current_user: dict = Depends(user_required),
    db: AsyncSession = Depends(get_db),
):
    try:
        result = await db.execute(
            select(User).where(User.username == current_user["sub"])
        )
        user = result.scalar_one()
        result = await db.execute(
            select(Notification).where(Notification.id == notification_id)
        )
        notification = result.scalar_one_or_none()
        if not notification:
            raise HTTPException(status_code=404, detail="Notification not found")
        if notification.user_id != user.id:
            raise HTTPException(status_code=403, detail="Access denied")
        notification.is_read = True
        await db.commit()
        await db.refresh(notification)
        return notification
    except HTTPException:
        raise
    except Exception:
        logging.error("Unable to mark notification as read", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.delete("/{notification_id}")
async def delete_notification(
    notification_id: str,
    current_user: dict = Depends(user_required),
    db: AsyncSession = Depends(get_db),
):
    try:
        result = await db.execute(
            select(User).where(User.username == current_user["sub"])
        )
        user = result.scalar_one()
        result = await db.execute(
            select(Notification).where(Notification.id == notification_id)
        )
        notification = result.scalar_one_or_none()
        if not notification:
            raise HTTPException(status_code=404, detail="Notification not found")
        if notification.user_id != user.id:
            raise HTTPException(status_code=403, detail="Access denied")
        await db.delete(notification)
        await db.commit()
        return {"status": "success", "response": "Notification deleted successfully"}
    except HTTPException:
        raise
    except Exception:
        logging.error("Unable to delete notification", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/all", response_model=list[NotificationResponse])
async def get_all_notifications(
    current_user: dict = Depends(admin_required), db: AsyncSession = Depends(get_db)
):
    try:
        result = await db.execute(select(Notification))
        notifications = result.scalars().all()
        return notifications
    except Exception:
        logging.error("Unable to fetch all notifications", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")
