import logging
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from models import Sport, Team, Match
from schemas import MatchCreate, MatchUpdate
from auth import admin_required

router = APIRouter()


@router.post("/")
async def create_match(
    match: MatchCreate,
    current_user: dict = Depends(admin_required),
    db: AsyncSession = Depends(get_db),
):
    try:
        result = await db.execute(select(Sport).where(Sport.id == match.sport_id))
        sport = result.scalar_one_or_none()
        if not sport:
            raise HTTPException(status_code=404, detail="Sport not found")
        result = await db.execute(select(Team).where(Team.id == match.team1_id))
        team1 = result.scalar_one_or_none()
        if not team1:
            raise HTTPException(status_code=404, detail="Team 1 not found")
        result = await db.execute(select(Team).where(Team.id == match.team2_id))
        team2 = result.scalar_one_or_none()
        if not team2:
            raise HTTPException(status_code=404, detail="Team 2 not found")
        if match.team1_id == match.team2_id:
            raise HTTPException(status_code=400, detail="Teams must be different")
        new_match = Match(
            sport_id=match.sport_id,
            team1_id=match.team1_id,
            team2_id=match.team2_id,
            match_name=match.match_name,
            start_time=match.start_time,
            end_time=match.end_time,
            status="upcoming",
        )
        db.add(new_match)
        await db.commit()
        await db.refresh(new_match)
        return {
            "status": "success",
            "response": "Match created successfully",
            "data": {
                "id": new_match.id,
                "sport_id": new_match.sport_id,
                "team1_id": new_match.team1_id,
                "team2_id": new_match.team2_id,
                "match_name": new_match.match_name,
                "start_time": new_match.start_time,
                "end_time": new_match.end_time,
                "status": new_match.status,
            },
        }
    except HTTPException:
        raise
    except Exception:
        logging.error("Match creation failed", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/")
async def get_matches(db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(select(Match))
        matches = result.scalars().all()
        return {
            "status": "success",
            "response": "Matches fetched successfully",
            "data": matches,
        }
    except Exception:
        logging.error("Unable to fetch matches", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/{match_id}")
async def get_match(match_id: str, db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(select(Match).where(Match.id == match_id))
        match = result.scalar_one_or_none()
        if not match:
            raise HTTPException(status_code=404, detail="Match not found")
        return {
            "status": "success",
            "response": "Match fetched successfully",
            "data": match,
        }
    except HTTPException:
        raise
    except Exception:
        logging.error("Unable to fetch match", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.put("/{match_id}")
async def update_match(
    match_id: str,
    match: MatchUpdate,
    current_user: dict = Depends(admin_required),
    db: AsyncSession = Depends(get_db),
):
    try:
        result = await db.execute(select(Match).where(Match.id == match_id))
        existing_match = result.scalar_one_or_none()
        if not existing_match:
            raise HTTPException(status_code=404, detail="Match not found")
        result = await db.execute(select(Sport).where(Sport.id == match.sport_id))
        sport = result.scalar_one_or_none()
        if not sport:
            raise HTTPException(status_code=404, detail="Sport not found")
        result = await db.execute(select(Team).where(Team.id == match.team1_id))
        team1 = result.scalar_one_or_none()
        if not team1:
            raise HTTPException(status_code=404, detail="Team 1 not found")
        result = await db.execute(select(Team).where(Team.id == match.team2_id))
        team2 = result.scalar_one_or_none()
        if not team2:
            raise HTTPException(status_code=404, detail="Team 2 not found")
        if match.team1_id == match.team2_id:
            raise HTTPException(status_code=400, detail="Teams must be different")
        existing_match.sport_id = match.sport_id
        existing_match.team1_id = match.team1_id
        existing_match.team2_id = match.team2_id
        existing_match.match_name = match.match_name
        existing_match.start_time = match.start_time
        existing_match.end_time = match.end_time
        await db.commit()
        await db.refresh(existing_match)
        return {
            "status": "success",
            "response": "Match updated successfully",
            "data": existing_match,
        }
    except HTTPException:
        raise
    except Exception:
        logging.error("Unable to update match", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.delete("/{match_id}")
async def delete_match(
    match_id: str,
    current_user: dict = Depends(admin_required),
    db: AsyncSession = Depends(get_db),
):
    try:
        result = await db.execute(select(Match).where(Match.id == match_id))
        match = result.scalar_one_or_none()
        if not match:
            raise HTTPException(status_code=404, detail="Match not found")
        await db.delete(match)
        await db.commit()
        return {"status": "success", "response": "Match deleted successfully"}
    except HTTPException:
        raise
    except Exception:
        logging.error("Unable to delete match", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")
