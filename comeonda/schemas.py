from sqlalchemy import (
    String,
    Integer
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from database import Base


class User(Base):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    name: Mapped[str] = mapped_column(
        String(100)
    )

    username: Mapped[str] = mapped_column(
        String(50),
        unique=True
    )

    email: Mapped[str] = mapped_column(
        String(100),
        unique=True
    )

    password: Mapped[str] = mapped_column(
        String(255)
    )

    role: Mapped[str] = mapped_column(
        String(20),
        default="user"
    )

    points: Mapped[int] = mapped_column(
        Integer,
        default=500
    )