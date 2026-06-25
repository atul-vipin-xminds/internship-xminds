import logging
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select, desc
from sqlalchemy.ext.asyncio import AsyncSession
from auth import admin_required, user_required
from database import get_db
from models import User

router = APIRouter()


@router.get("/global")
async def global_leaderboard(db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(select(User).order_by(desc(User.points)))
        users = result.scalars().all()
        leaderboard = []
        rank = 1
        for user in users:
            leaderboard.append(
                {
                    "rank": rank,
                    "user_id": user.id,
                    "username": user.username,
                    "points": user.points,
                }
            )
            rank += 1
        return {
            "status": "success",
            "response": "Global leaderboard fetched successfully",
            "data": leaderboard,
        }
    except Exception:
        logging.error("Unable to fetch global leaderboard", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/top/{count}")
async def top_players(count: int, db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(select(User).order_by(desc(User.points)).limit(count))
        users = result.scalars().all()
        leaderboard = []
        rank = 1
        for user in users:
            leaderboard.append(
                {
                    "rank": rank,
                    "user_id": user.id,
                    "username": user.username,
                    "points": user.points,
                }
            )
            rank += 1
        return {
            "status": "success",
            "response": f"Top {count} players fetched successfully",
            "data": leaderboard,
        }
    except Exception:
        logging.error("Unable to fetch top players", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/me")
async def my_rank(
    current_user: dict = Depends(user_required), db: AsyncSession = Depends(get_db)
):
    try:
        result = await db.execute(select(User).order_by(desc(User.points)))
        users = result.scalars().all()
        rank = 1
        for user in users:
            if user.username == current_user["sub"]:
                return {
                    "status": "success",
                    "data": {
                        "rank": rank,
                        "user_id": user.id,
                        "username": user.username,
                        "points": user.points,
                    },
                }
            rank += 1
        raise HTTPException(status_code=404, detail="User not found")
    except HTTPException:
        raise
    except Exception:
        logging.error("Unable to fetch user rank", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")
