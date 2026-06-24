import logging
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from models import Match, Question, Option
from schemas import QuestionCreate
from auth import admin_required


router = APIRouter()


@router.post("/")
async def create_question(
    question: QuestionCreate,
    current_user: dict = Depends(admin_required),
    db: AsyncSession = Depends(get_db)
):

    try:

        result = await db.execute(
            select(Match).where(
                Match.id == question.match_id
            )
        )

        match = result.scalar_one_or_none()

        if not match:

            raise HTTPException(
                status_code=404,
                detail="Match not found"
            )

        if len(question.options) != 4:

            raise HTTPException(
                status_code=400,
                detail="Question must contain exactly 4 options"
            )

        new_question = Question(
            match_id=question.match_id,
            question_text=question.question_text,
            entry_fee=question.entry_fee,
            start_time=question.start_time,
            end_time=question.end_time,
            status="active"
        )

        db.add(
            new_question
        )

        await db.commit()

        await db.refresh(
            new_question
        )

        created_options = []

        for option_text in question.options:

            option = Option(
                question_id=new_question.id,
                option_text=option_text
            )

            db.add(
                option
            )

            created_options.append(
                option_text
            )

        await db.commit()

        return {
            "status": "success",
            "response": "Question created successfully",
            "data": {
                "id": new_question.id,
                "match_id": new_question.match_id,
                "question_text": new_question.question_text,
                "entry_fee": new_question.entry_fee,
                "start_time": new_question.start_time,
                "end_time": new_question.end_time,
                "status": new_question.status,
                "options": created_options
            }
        }

    except HTTPException:

        raise

    except Exception:

        logging.error(
            "Question creation failed",
            exc_info=True
        )

        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )


@router.get("/")
async def get_questions(
    db: AsyncSession = Depends(get_db)
):

    try:

        current_time = datetime.now()

        result = await db.execute(
            select(Question).where(
                Question.start_time <= current_time,
                Question.end_time >= current_time,
                Question.status == "active"
            )
        )

        questions = (
            result.scalars().all()
        )

        return {
            "status": "success",
            "response": "Questions fetched successfully",
            "data": questions
        }

    except Exception:

        logging.error(
            "Unable to fetch questions",
            exc_info=True
        )

        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )


@router.get("/{question_id}")
async def get_question(
    question_id: str,
    db: AsyncSession = Depends(get_db)
):

    try:

        result = await db.execute(
            select(Question).where(
                Question.id == question_id
            )
        )

        question = result.scalar_one_or_none()

        if not question:

            raise HTTPException(
                status_code=404,
                detail="Question not found"
            )

        return {
            "status": "success",
            "response": "Question fetched successfully",
            "data": question
        }

    except HTTPException:

        raise

    except Exception:

        logging.error(
            "Unable to fetch question",
            exc_info=True
        )

        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )