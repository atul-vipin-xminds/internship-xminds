from datetime import date

from sqlalchemy import (
    ForeignKey,
    String
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship
)

from database import Base


class User(Base):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    name: Mapped[str] = mapped_column(
        String(100)
    )

    username: Mapped[str] = mapped_column(
        String(100),
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
        String(50)
    )

    leaves: Mapped[list["LeaveRequest"]] = relationship(
        back_populates="employee",
        cascade="all, delete-orphan"
    )


class LeaveRequest(Base):

    __tablename__ = "leave_requests"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        index=True
    )

    leave_date: Mapped[date] = mapped_column()

    reason: Mapped[str] = mapped_column(
        String(255)
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="pending"
    )

    employee_id: Mapped[int] = mapped_column(
        ForeignKey("users.id")
    )

    employee: Mapped["User"] = relationship(
        back_populates="leaves"
    )