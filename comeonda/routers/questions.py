import logging
from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from models import Match, Question, Option
from schemas import QuestionCreate, QuestionUpdate
from auth import admin_required

router = APIRouter()


@router.post("/")
async def create_question(
    question: QuestionCreate,
    current_user: dict = Depends(admin_required),
    db: AsyncSession = Depends(get_db),
):
    try:
        result = await db.execute(select(Match).where(Match.id == question.match_id))
        match = result.scalar_one_or_none()
        if not match:
            raise HTTPException(status_code=404, detail="Match not found")
        if len(question.options) != 4:
            raise HTTPException(
                status_code=400, detail="Question must contain exactly 4 options"
            )
        new_question = Question(
            match_id=question.match_id,
            question_text=question.question_text,
            entry_fee=question.entry_fee,
            start_time=question.start_time,
            end_time=question.end_time,
            status="upcoming",
        )
        db.add(new_question)
        await db.commit()
        await db.refresh(new_question)
        created_options = []
        for option_text in question.options:
            option = Option(question_id=new_question.id, option_text=option_text)
            db.add(option)
            created_options.append(option_text)
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
                "options": created_options,
            },
        }
    except HTTPException:
        raise
    except Exception:
        logging.error("Question creation failed", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/")
async def get_questions(db: AsyncSession = Depends(get_db)):
    try:
        current_time = datetime.now()
        result = await db.execute(select(Question))
        questions = result.scalars().all()
        active_questions = []
        for question in questions:
            if current_time < question.start_time:
                question.status = "upcoming"
            elif question.start_time <= current_time <= question.end_time:
                question.status = "active"
                active_questions.append(question)
            else:
                question.status = "closed"
        await db.commit()
        return {
            "status": "success",
            "response": "Questions fetched successfully",
            "data": active_questions,
        }
    except Exception:
        logging.error("Unable to fetch questions", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/{question_id}")
async def get_question(question_id: str, db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(select(Question).where(Question.id == question_id))
        question = result.scalar_one_or_none()
        if not question:
            raise HTTPException(status_code=404, detail="Question not found")
        current_time = datetime.now()
        if current_time < question.start_time:
            question.status = "upcoming"
        elif question.start_time <= current_time <= question.end_time:
            question.status = "active"
        else:
            question.status = "closed"
        await db.commit()
        return {
            "status": "success",
            "response": "Question fetched successfully",
            "data": question,
        }
    except HTTPException:
        raise
    except Exception:
        logging.error("Unable to fetch question", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.put("/{question_id}")
async def update_question(
    question_id: str,
    question: QuestionUpdate,
    current_user: dict = Depends(admin_required),
    db: AsyncSession = Depends(get_db),
):
    try:
        result = await db.execute(select(Question).where(Question.id == question_id))
        existing_question = result.scalar_one_or_none()
        if not existing_question:
            raise HTTPException(status_code=404, detail="Question not found")
        if len(question.options) != 4:
            raise HTTPException(
                status_code=400, detail="Question must contain exactly 4 options"
            )
        existing_question.question_text = question.question_text
        existing_question.entry_fee = question.entry_fee
        existing_question.start_time = question.start_time
        existing_question.end_time = question.end_time
        result = await db.execute(
            select(Option).where(Option.question_id == question_id)
        )
        old_options = result.scalars().all()
        for option in old_options:
            await db.delete(option)
        await db.flush()
        created_options = []
        for option_text in question.options:
            option = Option(question_id=question_id, option_text=option_text)
            db.add(option)
            created_options.append(option_text)
        await db.commit()
        await db.refresh(existing_question)
        return {
            "status": "success",
            "response": "Question updated successfully",
            "data": {
                "id": existing_question.id,
                "match_id": existing_question.match_id,
                "question_text": existing_question.question_text,
                "entry_fee": existing_question.entry_fee,
                "start_time": existing_question.start_time,
                "end_time": existing_question.end_time,
                "status": existing_question.status,
                "options": created_options,
            },
        }
    except HTTPException:
        raise
    except Exception:
        logging.error("Unable to update question", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.delete("/{question_id}")
async def delete_question(
    question_id: str,
    current_user: dict = Depends(admin_required),
    db: AsyncSession = Depends(get_db),
):
    try:
        result = await db.execute(select(Question).where(Question.id == question_id))
        question = result.scalar_one_or_none()
        if not question:
            raise HTTPException(status_code=404, detail="Question not found")
        await db.delete(question)
        await db.commit()
        return {"status": "success", "response": "Question deleted successfully"}
    except HTTPException:
        raise
    except Exception:
        logging.error("Unable to delete question", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")
