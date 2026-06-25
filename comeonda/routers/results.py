import logging
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from auth import admin_required, user_required
from database import get_db
from models import Result, Question, Option, Answer, User, Notification
from schemas import ResultCreate, ResultResponse

router = APIRouter()


@router.post("/", response_model=ResultResponse)
async def declare_result(
    result: ResultCreate,
    current_user: dict = Depends(admin_required),
    db: AsyncSession = Depends(get_db),
):
    try:
        question_result = await db.execute(
            select(Question).where(Question.id == result.question_id)
        )
        question = question_result.scalar_one_or_none()
        if not question:
            raise HTTPException(status_code=404, detail="Question not found")
        option_result = await db.execute(
            select(Option).where(Option.id == result.correct_option_id)
        )
        option = option_result.scalar_one_or_none()
        if not option:
            raise HTTPException(status_code=404, detail="Option not found")
        if option.question_id != question.id:
            raise HTTPException(
                status_code=400, detail="Option does not belong to question"
            )
        existing_result = await db.execute(
            select(Result).where(Result.question_id == result.question_id)
        )
        if existing_result.scalar_one_or_none():
            raise HTTPException(status_code=400, detail="Result already declared")
        admin_result = await db.execute(
            select(User).where(User.username == current_user["sub"])
        )
        admin = admin_result.scalar_one()
        new_result = Result(
            question_id=result.question_id,
            correct_option_id=result.correct_option_id,
            declared_by=admin.id,
        )
        db.add(new_result)
        answer_result = await db.execute(
            select(Answer).where(Answer.question_id == result.question_id)
        )
        answers = answer_result.scalars().all()
        for answer in answers:
            if answer.option_id == result.correct_option_id:
                notification = Notification(
                    user_id=answer.user_id,
                    title="Result Declared",
                    message="Congratulations! Your prediction was correct.",
                )
            else:
                notification = Notification(
                    user_id=answer.user_id,
                    title="Result Declared",
                    message="Your prediction was incorrect. Better luck next time!",
                )
            db.add(notification)
        await db.commit()
        await db.refresh(new_result)
        return {
            "status": "success",
            "response": "Result declared successfully",
            "data": new_result,
        }
    except HTTPException:
        raise
    except Exception:
        logging.error("Unable to declare result", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/{question_id}", response_model=ResultResponse)
async def get_result(question_id: str, db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(
            select(Result).where(Result.question_id == question_id)
        )
        declared_result = result.scalar_one_or_none()
        if not declared_result:
            raise HTTPException(status_code=404, detail="Result not declared")
        return declared_result
    except HTTPException:
        raise
    except Exception:
        logging.error("Unable to fetch result", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/my-result/{question_id}")
async def my_result(
    question_id: str,
    current_user: dict = Depends(user_required),
    db: AsyncSession = Depends(get_db),
):
    try:
        user_result = await db.execute(
            select(User).where(User.username == current_user["sub"])
        )
        user = user_result.scalar_one()
        answer_result = await db.execute(
            select(Answer).where(
                Answer.user_id == user.id, Answer.question_id == question_id
            )
        )
        answer = answer_result.scalar_one_or_none()
        if not answer:
            raise HTTPException(
                status_code=404, detail="You have not answered this question"
            )
        result_query = await db.execute(
            select(Result).where(Result.question_id == question_id)
        )
        declared_result = result_query.scalar_one_or_none()
        if not declared_result:
            raise HTTPException(status_code=404, detail="Result not declared yet")
        return {
            "status": "success",
            "question_id": question_id,
            "your_option": answer.option_id,
            "correct_option": declared_result.correct_option_id,
            "won": answer.option_id == declared_result.correct_option_id,
        }
    except HTTPException:
        raise
    except Exception:
        logging.error("Unable to fetch user result", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")
