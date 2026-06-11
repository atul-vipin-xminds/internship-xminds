from fastapi import FastAPI
from models import StudentCreate, StudentResponse

app = FastAPI()


@app.get("/greet")
def greet(name: str):
    return {"message": f"Hello {name}"}


@app.post("/greet")
def greet_post(name: str):
    return {"message": f"Hello {name}"}


@app.post("/student")
def create_student(student: dict):
    return {
        "name": student["name"],
        "course": student["course"]
    }


# Response Model Example
@app.post("/students", response_model=StudentResponse)
def create_students(student: StudentCreate):
    new_student = {
        "id": 101,
        "name": student.name,
        "course": student.course,
        "email": student.email
    }
    return new_student


@app.post("/student/{course_id}", response_model=StudentResponse)
def create_student_with_id(course_id: int, student: StudentCreate):
    return {
        "id": course_id,
        "name": student.name,
        "course": student.course,
        "email": student.email
    }


@app.put("/student/{course_id}", response_model=StudentResponse)
def update_student(course_id: int, student: StudentCreate):
    return {
        "id": course_id,
        "name": student.name,
        "course": student.course,
        "email": student.email
    }


@app.get("/students", response_model=list[StudentResponse])
def get_students():
    return [
        {
            "id": 1,
            "name": "Atul",
            "course": "Python",
            "email": "atul@gmail.com"
        },
        {
            "id": 2,
            "name": "Rahul",
            "course": "FastAPI",
            "email": "rahul@gmail.com"
        }
    ]