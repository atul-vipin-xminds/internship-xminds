import logging
import random
import string
from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from schemas import UserCreate
from database import get_db
from config import settings
from models import User, PointHistory, Notification
from jwt_utils import hash_password, verify_password, create_access_token
from auth import get_current_user

router = APIRouter()
conf = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=settings.MAIL_PASSWORD,
    MAIL_FROM=settings.MAIL_FROM,
    MAIL_PORT=settings.MAIL_PORT,
    MAIL_SERVER=settings.MAIL_SERVER,
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
)


def generate_referral_code():
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=8))


async def send_welcome_email(email: str):
    message = MessageSchema(
        subject="Welcome to Come On Da",
        recipients=[email],
        body="""
Welcome to Come On Da.
Your account has been created successfully.
""",
        subtype="plain",
    )
    fm = FastMail(conf)
    await fm.send_message(message)


async def send_referral_reward_email(email: str):
    message = MessageSchema(
        subject="Referral Reward",
        recipients=[email],
        body="""
Congratulations!
You earned 100 points because a user joined using your referral code.
""",
        subtype="plain",
    )
    fm = FastMail(conf)
    await fm.send_message(message)


@router.post("/register")
async def register_user(
    user: UserCreate,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db),
):
    try:
        result = await db.execute(select(User).where(User.username == user.username))
        existing_user = result.scalar_one_or_none()
        if existing_user:
            raise HTTPException(status_code=400, detail="Username already exists")
        referral_code = generate_referral_code()
        referred_by = None
        if user.referral_code:
            result = await db.execute(
                select(User).where(User.referral_code == user.referral_code)
            )
            inviter = result.scalar_one_or_none()
            if inviter:
                inviter.points += 100
                referred_by = inviter.id
                referral_history = PointHistory(
                    user_id=inviter.id,
                    points=100,
                    transaction_type="referral_reward",
                    description="Referral reward",
                )
                db.add(referral_history)
                referral_notification = Notification(
                    user_id=inviter.id,
                    title="Referral Bonus",
                    message="You earned 100 points for referring a new user.",
                )
                db.add(referral_notification)
                background_tasks.add_task(send_referral_reward_email, inviter.email)
        new_user = User(
            name=user.name,
            username=user.username,
            email=user.email,
            password=hash_password(user.password),
            role="user",
            points=500,
            device_id=user.device_id,
            referral_code=referral_code,
            referred_by=referred_by,
        )
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
        signup_history = PointHistory(
            user_id=new_user.id,
            points=500,
            transaction_type="signup",
            description="Signup bonus",
        )
        db.add(signup_history)
        welcome_notification = Notification(
            user_id=new_user.id,
            title="Welcome",
            message="Welcome to Come On Da! Your account has been created successfully.",
        )
        db.add(welcome_notification)
        await db.commit()
        background_tasks.add_task(send_welcome_email, user.email)
        token = create_access_token({"sub": new_user.username, "role": new_user.role})
        user_data = {
            "id": new_user.id,
            "name": new_user.name,
            "username": new_user.username,
            "email": new_user.email,
            "role": new_user.role,
            "points": new_user.points,
            "device_id": new_user.device_id,
            "referral_code": new_user.referral_code,
        }
        return {
            "status": "success",
            "response": f"Successfully registered with username {new_user.username}",
            "access_token": token,
            "user_details": user_data,
        }
    except HTTPException:
        raise
    except Exception:
        logging.error("User not able to register", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(get_db)
):
    try:
        result = await db.execute(
            select(User).where(User.username == form_data.username)
        )
        db_user = result.scalar_one_or_none()
        if not db_user:
            raise HTTPException(status_code=401, detail="Invalid username")
        if not verify_password(form_data.password, db_user.password):
            raise HTTPException(status_code=401, detail="Invalid password")
        token = create_access_token({"sub": db_user.username, "role": db_user.role})
        user_data = {
            "id": db_user.id,
            "name": db_user.name,
            "username": db_user.username,
            "email": db_user.email,
            "role": db_user.role,
            "points": db_user.points,
            "device_id": db_user.device_id,
            "referral_code": db_user.referral_code,
        }
        return {"status": "success", "access_token": token, "user_details": user_data}
    except HTTPException:
        raise
    except Exception:
        logging.error("User not able to login", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/profile")
async def profile(
    current_user: dict = Depends(get_current_user), db: AsyncSession = Depends(get_db)
):
    try:
        result = await db.execute(
            select(User).where(User.username == current_user["sub"])
        )
        user = result.scalar_one_or_none()
        return {
            "status": "success",
            "user_details": {
                "id": user.id,
                "name": user.name,
                "username": user.username,
                "email": user.email,
                "role": user.role,
                "points": user.points,
                "device_id": user.device_id,
                "referral_code": user.referral_code,
                "referred_by": user.referred_by,
            },
        }
    except Exception:
        logging.error("Unable to fetch profile", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")
