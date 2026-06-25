import uuid
from datetime import datetime
from sqlalchemy import String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base


class User(Base):
    __tablename__ = "users"
    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True
    )
    name: Mapped[str] = mapped_column(String(100))
    username: Mapped[str] = mapped_column(String(50), unique=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(255))
    role: Mapped[str] = mapped_column(String(20), default="user")
    points: Mapped[int] = mapped_column(Integer, default=500)
    device_id: Mapped[str] = mapped_column(String(255), nullable=True)
    referral_code: Mapped[str] = mapped_column(String(20), unique=True)
    referred_by: Mapped[str] = mapped_column(String(36), nullable=True)


class Sport(Base):
    __tablename__ = "sports"
    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True
    )
    name: Mapped[str] = mapped_column(String(100), unique=True)
    teams = relationship("Team", back_populates="sport", cascade="all, delete-orphan")
    matches = relationship(
        "Match", back_populates="sport", cascade="all, delete-orphan"
    )


class Team(Base):
    __tablename__ = "teams"
    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True
    )
    sport_id: Mapped[str] = mapped_column(ForeignKey("sports.id"))
    team_name: Mapped[str] = mapped_column(String(100))
    sport = relationship("Sport", back_populates="teams")


class Match(Base):
    __tablename__ = "matches"
    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True
    )
    sport_id: Mapped[str] = mapped_column(ForeignKey("sports.id"))
    team1_id: Mapped[str] = mapped_column(ForeignKey("teams.id"))
    team2_id: Mapped[str] = mapped_column(ForeignKey("teams.id"))
    match_name: Mapped[str] = mapped_column(String(255))
    start_time: Mapped[DateTime] = mapped_column(DateTime)
    end_time: Mapped[DateTime] = mapped_column(DateTime)
    status: Mapped[str] = mapped_column(String(20), default="upcoming")
    sport = relationship("Sport", back_populates="matches")
    questions = relationship(
        "Question", back_populates="match", cascade="all, delete-orphan"
    )


class Question(Base):
    __tablename__ = "questions"
    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True
    )
    match_id: Mapped[str] = mapped_column(ForeignKey("matches.id"))
    question_text: Mapped[str] = mapped_column(String(255))
    entry_fee: Mapped[int] = mapped_column(Integer, default=100)
    start_time: Mapped[DateTime] = mapped_column(DateTime)
    end_time: Mapped[DateTime] = mapped_column(DateTime)
    status: Mapped[str] = mapped_column(String(20), default="active")
    match = relationship("Match", back_populates="questions")
    options = relationship(
        "Option", back_populates="question", cascade="all, delete-orphan"
    )


class Option(Base):
    __tablename__ = "options"
    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True
    )
    question_id: Mapped[str] = mapped_column(ForeignKey("questions.id"))
    option_text: Mapped[str] = mapped_column(String(100))
    question = relationship("Question", back_populates="options")


class Answer(Base):
    __tablename__ = "answers"
    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True
    )
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    question_id: Mapped[str] = mapped_column(ForeignKey("questions.id"))
    option_id: Mapped[str] = mapped_column(ForeignKey("options.id"))
    submitted_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.utcnow)


class Result(Base):
    __tablename__ = "results"
    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True
    )
    question_id: Mapped[str] = mapped_column(ForeignKey("questions.id"), unique=True)
    correct_option_id: Mapped[str] = mapped_column(ForeignKey("options.id"))
    declared_by: Mapped[str] = mapped_column(ForeignKey("users.id"))
    declared_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.utcnow)


class PointHistory(Base):
    __tablename__ = "point_history"
    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True
    )
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    points: Mapped[int] = mapped_column(Integer)
    transaction_type: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.utcnow)


class Notification(Base):
    __tablename__ = "notifications"
    id: Mapped[str] = mapped_column(
        String(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True
    )
    user_id: Mapped[str] = mapped_column(ForeignKey("users.id"))
    title: Mapped[str] = mapped_column(String(100))
    message: Mapped[str] = mapped_column(String(255))
    is_read: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.utcnow)
