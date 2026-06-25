import logging
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from auth import admin_required, user_required
from database import get_db
from models import Sport
from schemas import SportCreate, SportUpdate

router = APIRouter()


@router.post("/")
async def create_sport(
    sport: SportCreate,
    current_user: dict = Depends(admin_required),
    db: AsyncSession = Depends(get_db),
):
    try:
        result = await db.execute(select(Sport).where(Sport.name == sport.name))
        existing_sport = result.scalar_one_or_none()
        if existing_sport:
            raise HTTPException(status_code=400, detail="Sport already exists")
        new_sport = Sport(name=sport.name)
        db.add(new_sport)
        await db.commit()
        await db.refresh(new_sport)
        return {
            "status": "success",
            "response": "Sport created successfully",
            "data": {"id": new_sport.id, "name": new_sport.name},
        }
    except HTTPException:
        raise
    except Exception:
        logging.error("Sport creation failed", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/")
async def get_sports(db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(select(Sport))
        sports = result.scalars().all()
        return {
            "status": "success",
            "response": "Sports fetched successfully",
            "data": sports,
        }
    except Exception:
        logging.error("Unable to fetch sports", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/{sport_id}")
async def get_sport(sport_id: str, db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(select(Sport).where(Sport.id == sport_id))
        sport = result.scalar_one_or_none()
        if not sport:
            raise HTTPException(status_code=404, detail="Sport not found")
        return {
            "status": "success",
            "response": "Sport fetched successfully",
            "data": sport,
        }
    except HTTPException:
        raise
    except Exception:
        logging.error("Unable to fetch sport", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.put("/{sport_id}")
async def update_sport(
    sport_id: str,
    sport: SportUpdate,
    current_user: dict = Depends(admin_required),
    db: AsyncSession = Depends(get_db),
):
    try:
        result = await db.execute(select(Sport).where(Sport.id == sport_id))
        existing_sport = result.scalar_one_or_none()
        if not existing_sport:
            raise HTTPException(status_code=404, detail="Sport not found")
        result = await db.execute(
            select(Sport).where(Sport.name == sport.name, Sport.id != sport_id)
        )
        duplicate = result.scalar_one_or_none()
        if duplicate:
            raise HTTPException(status_code=400, detail="Sport already exists")
        existing_sport.name = sport.name
        await db.commit()
        await db.refresh(existing_sport)
        return {
            "status": "success",
            "response": "Sport updated successfully",
            "data": existing_sport,
        }
    except HTTPException:
        raise
    except Exception:
        logging.error("Unable to update sport", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.delete("/{sport_id}")
async def delete_sport(
    sport_id: str,
    current_user: dict = Depends(admin_required),
    db: AsyncSession = Depends(get_db),
):
    try:
        result = await db.execute(select(Sport).where(Sport.id == sport_id))
        sport = result.scalar_one_or_none()
        if not sport:
            raise HTTPException(status_code=404, detail="Sport not found")
        await db.delete(sport)
        await db.commit()
        return {"status": "success", "response": "Sport deleted successfully"}
    except HTTPException:
        raise
    except Exception:
        logging.error("Unable to delete sport", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")
