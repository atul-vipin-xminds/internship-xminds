import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from models import User, Question, Option, Answer
from schemas import AnswerCreate
from auth import user_required


router = APIRouter()


@router.post("/")
async def submit_answer(
    answer: AnswerCreate,
    current_user: dict = Depends(
        user_required
    ),
    db: AsyncSession = Depends(
        get_db
    )
):

    try:

        result = await db.execute(
            select(User).where(
                User.username ==
                current_user["sub"]
            )
        )

        user = result.scalar_one_or_none()

        if not user:

            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        if user.points < 100:

            raise HTTPException(
                status_code=400,
                detail="Not enough points"
            )

        result = await db.execute(
            select(Question).where(
                Question.id ==
                answer.question_id
            )
        )

        question = result.scalar_one_or_none()

        if not question:

            raise HTTPException(
                status_code=404,
                detail="Question not found"
            )

        result = await db.execute(
            select(Option).where(
                Option.id ==
                answer.option_id
            )
        )

        option = result.scalar_one_or_none()

        if not option:

            raise HTTPException(
                status_code=404,
                detail="Option not found"
            )

        if option.question_id != answer.question_id:

            raise HTTPException(
                status_code=400,
                detail="Option does not belong to question"
            )

        result = await db.execute(
            select(Answer).where(
                Answer.user_id == user.id,
                Answer.question_id ==
                answer.question_id
            )
        )

        existing_answer = (
            result.scalar_one_or_none()
        )

        if existing_answer:

            raise HTTPException(
                status_code=400,
                detail="Already answered"
            )

        user.points -= 100

        new_answer = Answer(
            user_id=user.id,
            question_id=answer.question_id,
            option_id=answer.option_id
        )

        db.add(
            new_answer
        )

        await db.commit()

        await db.refresh(
            new_answer
        )

        return {
            "status": "success",
            "response": "Answer submitted successfully",
            "data": {
                "id": new_answer.id,
                "user_id": new_answer.user_id,
                "question_id": new_answer.question_id,
                "option_id": new_answer.option_id,
                "remaining_points": user.points
            }
        }

    except HTTPException:

        raise

    except Exception:

        logging.error(
            "Answer submission failed",
            exc_info=True
        )

        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )


@router.get("/my-history")
async def my_history(
    current_user: dict = Depends(
        user_required
    ),
    db: AsyncSession = Depends(
        get_db
    )
):

    try:

        result = await db.execute(
            select(User).where(
                User.username ==
                current_user["sub"]
            )
        )

        user = result.scalar_one_or_none()

        if not user:

            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        result = await db.execute(
            select(Answer).where(
                Answer.user_id == user.id
            )
        )

        answers = (
            result.scalars().all()
        )

        return {
            "status": "success",
            "response": "History fetched successfully",
            "data": answers
        }

    except HTTPException:

        raise

    except Exception:

        logging.error(
            "Unable to fetch answer history",
            exc_info=True
        )

        raise HTTPException(
            status_code=500,
            detail="Internal server error"
        )