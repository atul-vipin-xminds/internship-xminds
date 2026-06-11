from pydantic import BaseModel
from typing import Optional


class Address(BaseModel):
    city: str
    state: str


# Request Model
class StudentCreate(BaseModel):
    name: str
    age: int
    course: str
    email: Optional[str] = None
    courses: list[str] = []
    address: Address


# Response Model
class StudentResponse(BaseModel):
    id: int
    name: str
    course: str
    email: Optional[str] = None