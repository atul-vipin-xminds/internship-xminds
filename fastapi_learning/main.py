from fastapi import FastAPI
from models import Student

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


@app.post("/students")
def create_students(student: Student):
    return student


@app.post("/student/{course_id}")
def create_student_with_id(course_id: int, student: Student):
    return {
        "course_id": course_id,
        "student": student
    }
