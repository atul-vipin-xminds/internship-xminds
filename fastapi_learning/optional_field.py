from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int
    course: str
    email: Optional[str] = None

@app.post("/students")
def create_student(student: Student):
    return student