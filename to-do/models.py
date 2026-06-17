from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    Table
)
from sqlalchemy.orm import relationship
from database import Base


task_tag = Table(
    "task_tag",
    Base.metadata,
    Column(
        "task_id",
        Integer,
        ForeignKey("tasks.id")
    ),
    Column(
        "tag_id",
        Integer,
        ForeignKey("tags.id")
    )
)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    name = Column(String(100))

    username = Column(
        String(100),
        unique=True
    )

    email = Column(String(100))

    password = Column(String(255))

    role = Column(String(50))

    tasks = relationship(
        "Task",
        back_populates="user"
    )


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)

    title = Column(String(100))

    completed = Column(
        Boolean,
        default=False
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    user = relationship(
        "User",
        back_populates="tasks"
    )

    task_detail = relationship(
        "TaskDetail",
        back_populates="task",
        uselist=False
    )

    tags = relationship(
        "Tag",
        secondary=task_tag,
        back_populates="tasks"
    )


class TaskDetail(Base):
    __tablename__ = "task_details"

    id = Column(
        Integer,
        primary_key=True
    )

    description = Column(
        String(255)
    )

    due_date = Column(
        String(50)
    )

    task_id = Column(
        Integer,
        ForeignKey("tasks.id"),
        unique=True
    )

    task = relationship(
        "Task",
        back_populates="task_detail"
    )


class Tag(Base):
    __tablename__ = "tags"

    id = Column(
        Integer,
        primary_key=True
    )

    tag_name = Column(
        String(100)
    )

    tasks = relationship(
        "Task",
        secondary=task_tag,
        back_populates="tags"
    )