from contextlib import asynccontextmanager

from fastapi import FastAPI

from sqlalchemy import select

from database import Base, engine, SessionLocal

from models import User

from jwt_utils import hash_password

from routers import users, sports, teams, matches, questions, answers


@asynccontextmanager
async def lifespan(app: FastAPI):

    async with engine.begin() as conn:

        await conn.run_sync(Base.metadata.create_all)

    async with SessionLocal() as db:

        result = await db.execute(select(User).where(User.username == "admin"))

        admin_user = result.scalar_one_or_none()

        if not admin_user:

            admin = User(
                name="Admin",
                username="admin",
                email="admin@gmail.com",
                password=hash_password("admin123"),
                role="admin",
                points=0,
                device_id="admin-device",
                referral_code="ADMIN001",
                referred_by=None,
            )

            db.add(admin)

            await db.commit()

    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def home():

    return {"message": "Come On Da API"}


app.include_router(users.router, prefix="/users", tags=["Users"])

app.include_router(sports.router, prefix="/sports", tags=["Sports"])

app.include_router(teams.router, prefix="/teams", tags=["Teams"])

app.include_router(matches.router, prefix="/matches", tags=["Matches"])

app.include_router(questions.router, prefix="/questions", tags=["Questions"])

app.include_router(answers.router, prefix="/answers", tags=["Answers"])
