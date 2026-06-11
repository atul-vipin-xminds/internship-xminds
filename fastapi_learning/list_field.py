from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    courses: list[str]

@app.post("/students")
def create_student(student: Student):
    return student