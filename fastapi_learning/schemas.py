from pydantic import BaseModel
from typing import Optional


class StudentCreate(BaseModel):
    name: str
    age: int
    course: str
    email: Optional[str] = None


class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    course: str
    email: Optional[str]

    class Config:
        from_attributes = True