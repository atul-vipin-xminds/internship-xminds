from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Address(BaseModel):
    city: str
    state: str

class Student(BaseModel):
    name: str
    address: Address

@app.post("/student/{course_id}")
def create_student(course_id: int, student: Student):
    return {
        "course_id": course_id,
        "student": student
    }