from datetime import date

from pydantic import (
    BaseModel,
    EmailStr
)


# ---------------- USER ----------------

class UserCreate(BaseModel):

    name: str

    username: str

    email: EmailStr

    password: str


class UserLogin(BaseModel):

    username: str

    password: str


class UserResponse(BaseModel):

    id: int

    name: str

    username: str

    email: str

    role: str

    class Config:
        from_attributes = True


class TokenResponse(BaseModel):

    access_token: str

    token_type: str


# ---------------- LEAVE ----------------

class LeaveCreate(BaseModel):

    leave_date: date

    reason: str


class LeaveStatusUpdate(BaseModel):

    status: str


class LeaveResponse(BaseModel):

    id: int

    leave_date: date

    reason: str

    status: str

    employee_id: int

    class Config:
        from_attributes = True