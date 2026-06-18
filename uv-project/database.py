from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker
)

from sqlalchemy.orm import DeclarativeBase

from config import settings


class Base(DeclarativeBase):
    pass


engine = create_async_engine(
    settings.DATABASE_URL,
    echo=True
)


SessionLocal = async_sessionmaker(
    bind=engine,
    expire_on_commit=False
)


async def get_db():

    async with SessionLocal() as db:

        yield db