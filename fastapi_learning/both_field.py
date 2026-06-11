from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Address(BaseModel):
    city: str
    state: str

class Student(BaseModel):
    name: str
    address: Address

@app.post("/students")
def create_student(student: Student):
    return student