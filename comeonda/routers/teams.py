import logging
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from models import Sport, Team
from schemas import TeamCreate, TeamUpdate
from auth import admin_required, user_required

router = APIRouter()


@router.post("/")
async def create_team(
    team: TeamCreate,
    current_user: dict = Depends(admin_required),
    db: AsyncSession = Depends(get_db),
):
    try:
        result = await db.execute(select(Sport).where(Sport.id == team.sport_id))
        sport = result.scalar_one_or_none()
        if not sport:
            raise HTTPException(status_code=404, detail="Sport not found")
        result = await db.execute(
            select(Team).where(
                Team.team_name == team.team_name, Team.sport_id == team.sport_id
            )
        )
        existing_team = result.scalar_one_or_none()
        if existing_team:
            raise HTTPException(status_code=400, detail="Team already exists")
        new_team = Team(sport_id=team.sport_id, team_name=team.team_name)
        db.add(new_team)
        await db.commit()
        await db.refresh(new_team)
        return {
            "status": "success",
            "response": "Team created successfully",
            "data": {
                "id": new_team.id,
                "sport_id": new_team.sport_id,
                "team_name": new_team.team_name,
            },
        }
    except HTTPException:
        raise
    except Exception:
        logging.error("Team creation failed", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/")
async def get_teams(db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(select(Team))
        teams = result.scalars().all()
        return {
            "status": "success",
            "response": "Teams fetched successfully",
            "data": teams,
        }
    except Exception:
        logging.error("Unable to fetch teams", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/{team_id}")
async def get_team(team_id: str, db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(select(Team).where(Team.id == team_id))
        team = result.scalar_one_or_none()
        if not team:
            raise HTTPException(status_code=404, detail="Team not found")
        return {
            "status": "success",
            "response": "Team fetched successfully",
            "data": team,
        }
    except HTTPException:
        raise
    except Exception:
        logging.error("Unable to fetch team", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.put("/{team_id}")
async def update_team(
    team_id: str,
    team: TeamUpdate,
    current_user: dict = Depends(admin_required),
    db: AsyncSession = Depends(get_db),
):
    try:
        result = await db.execute(select(Team).where(Team.id == team_id))
        existing_team = result.scalar_one_or_none()
        if not existing_team:
            raise HTTPException(status_code=404, detail="Team not found")
        result = await db.execute(select(Sport).where(Sport.id == team.sport_id))
        sport = result.scalar_one_or_none()
        if not sport:
            raise HTTPException(status_code=404, detail="Sport not found")
        result = await db.execute(
            select(Team).where(
                Team.team_name == team.team_name,
                Team.sport_id == team.sport_id,
                Team.id != team_id,
            )
        )
        duplicate = result.scalar_one_or_none()
        if duplicate:
            raise HTTPException(status_code=400, detail="Team already exists")
        existing_team.sport_id = team.sport_id
        existing_team.team_name = team.team_name
        await db.commit()
        await db.refresh(existing_team)
        return {
            "status": "success",
            "response": "Team updated successfully",
            "data": existing_team,
        }
    except HTTPException:
        raise
    except Exception:
        logging.error("Unable to update team", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.delete("/{team_id}")
async def delete_team(
    team_id: str,
    current_user: dict = Depends(admin_required),
    db: AsyncSession = Depends(get_db),
):
    try:
        result = await db.execute(select(Team).where(Team.id == team_id))
        team = result.scalar_one_or_none()
        if not team:
            raise HTTPException(status_code=404, detail="Team not found")
        await db.delete(team)
        await db.commit()
        return {"status": "success", "response": "Team deleted successfully"}
    except HTTPException:
        raise
    except Exception:
        logging.error("Unable to delete team", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")
