from pydantic import BaseModel
from typing import Optional


class StudentProfileBase(BaseModel):
    address: str
    phone: str


class StudentProfileCreate(StudentProfileBase):
    pass


class StudentProfileResponse(StudentProfileBase):
    id: int

    class Config:
        from_attributes = True


class StudentBase(BaseModel):
    name: str
    age: int
    course: str
    email: Optional[str] = None
    department_id: int


class StudentCreate(StudentBase):
    pass


class StudentResponse(StudentBase):
    id: int
    profile: StudentProfileResponse | None = None

    class Config:
        from_attributes = True


class DepartmentCreate(BaseModel):
    name: str


class DepartmentResponse(BaseModel):
    id: int
    name: str
    students: list[StudentResponse] = []

    class Config:
        from_attributes = True