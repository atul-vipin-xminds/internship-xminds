from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import Base, engine, get_db
from models import Student, StudentProfile, Department
from schemas import (
    StudentCreate,
    StudentResponse,
    StudentProfileCreate,
    StudentProfileResponse,
    DepartmentCreate,
    DepartmentResponse
)

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {
        "message": "Student Management API"
    }


@app.post("/departments")
def create_department(
    department: DepartmentCreate,
    db: Session = Depends(get_db)
):
    db_department = Department(
        name=department.name
    )

    db.add(db_department)
    db.commit()
    db.refresh(db_department)

    return db_department


@app.get(
    "/departments/{department_id}",
    response_model=DepartmentResponse
)
def get_department(
    department_id: int,
    db: Session = Depends(get_db)
):
    return db.query(Department).filter(
        Department.id == department_id
    ).first()


@app.post(
    "/students",
    response_model=StudentResponse
)
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    department = db.query(Department).filter(
        Department.id == student.department_id
    ).first()

    if not department:
        return {
            "error": "Department not found"
        }

    db_student = Student(
        name=student.name,
        age=student.age,
        course=student.course,
        email=student.email,
        department_id=student.department_id
    )

    db.add(db_student)
    db.commit()
    db.refresh(db_student)

    return db_student


@app.get(
    "/students",
    response_model=list[StudentResponse]
)
def get_students(
    db: Session = Depends(get_db)
):
    return db.query(Student).all()


@app.get(
    "/students/{student_id}",
    response_model=StudentResponse
)
def get_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    return db.query(Student).filter(
        Student.id == student_id
    ).first()


@app.post(
    "/students/{student_id}/profile",
    response_model=StudentProfileResponse
)
def create_profile(
    student_id: int,
    profile: StudentProfileCreate,
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:
        return {
            "error": "Student not found"
        }

    db_profile = StudentProfile(
        address=profile.address,
        phone=profile.phone,
        student_id=student_id
    )

    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)

    return db_profile


@app.delete("/students/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if not student:
        return {
            "error": "Student not found"
        }

    db.delete(student)
    db.commit()

    return {
        "message": f"Student {student_id} deleted successfully"
    }

@app.delete("/departments/{department_id}")
def delete_department(
    department_id: int,
    db: Session = Depends(get_db)
):
    department = db.query(Department).filter(
        Department.id == department_id
    ).first()

    if not department:
        return {
            "error": "Department not found"
        }

    db.delete(department)
    db.commit()

    return {
        "message": f"Department {department_id} deleted successfully"
    }