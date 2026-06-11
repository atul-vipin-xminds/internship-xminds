from fastapi import FastAPI
from models import Student

app = FastAPI()


# GET example
@app.get("/greet")
def greet(name: str):
    return {"message": f"Hello {name}"}


# POST example using query parameter
@app.post("/greet")
def greet_post(name: str):
    return {"message": f"Hello {name}"}


# POST example using dictionary
@app.post("/student")
def create_student(student: dict):
    return {
        "name": student["name"],
        "course": student["course"]
    }


# POST example using Pydantic model
@app.post("/students")
def create_students(student: Student):
    return student


# Path parameter + Pydantic model
@app.post("/student/{course_id}")
def create_student_with_id(course_id: int, student: Student):
    return {
        "course_id": course_id,
        "student": student
    }