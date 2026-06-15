from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Table
)
from sqlalchemy.orm import relationship

from database import Base


student_course = Table(
    "student_course",
    Base.metadata,
    Column(
        "student_id",
        Integer,
        ForeignKey("students.id")
    ),
    Column(
        "course_id",
        Integer,
        ForeignKey("courses.id")
    )
)


class Department(Base):
    __tablename__ = "departments"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(String(100))

    students = relationship(
        "Student",
        back_populates="department",
        cascade="all, delete-orphan"
    )


class Course(Base):
    __tablename__ = "courses"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(String(100))

    students = relationship(
        "Student",
        secondary=student_course,
        back_populates="courses"
    )


class Student(Base):
    __tablename__ = "students"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String(100),
        nullable=False
    )

    age = Column(Integer)

    course = Column(String(100))

    email = Column(
        String(100),
        unique=True
    )

    department_id = Column(
        Integer,
        ForeignKey("departments.id")
    )

    department = relationship(
        "Department",
        back_populates="students"
    )

    profile = relationship(
        "StudentProfile",
        back_populates="student",
        uselist=False,
        cascade="all, delete-orphan"
    )

    courses = relationship(
        "Course",
        secondary=student_course,
        back_populates="students"
    )


class StudentProfile(Base):
    __tablename__ = "student_profiles"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    address = Column(String(255))

    phone = Column(String(20))

    student_id = Column(
        Integer,
        ForeignKey("students.id"),
        unique=True
    )

    student = relationship(
        "Student",
        back_populates="profile"
    )