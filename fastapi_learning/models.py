from pydantic import BaseModel
from typing import Optional


class Address(BaseModel):
    city: str
    state: str


class Student(BaseModel):
    name: str
    age: int
    course: str
    email: Optional[str] = None
    courses: list[str] = []
    address: Address