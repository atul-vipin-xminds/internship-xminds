from datetime import datetime
from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    name: str
    username: str
    email: EmailStr
    password: str
    device_id: str
    referral_code: str | None = None


class UserLogin(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    id: str
    name: str
    username: str
    email: EmailStr
    role: str
    points: int
    device_id: str | None
    referral_code: str
    referred_by: str | None

    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    access_token: str
    token_type: str


class SportCreate(BaseModel):
    name: str


class SportResponse(BaseModel):
    id: str
    name: str

    class Config:
        from_attributes = True


class TeamCreate(BaseModel):
    sport_id: str
    team_name: str


class TeamResponse(BaseModel):
    id: str
    sport_id: str
    team_name: str

    class Config:
        from_attributes = True


class MatchCreate(BaseModel):
    sport_id: str
    team1_id: str
    team2_id: str
    match_name: str
    start_time: datetime
    end_time: datetime


class MatchResponse(BaseModel):
    id: str
    sport_id: str
    team1_id: str
    team2_id: str
    match_name: str
    start_time: datetime
    end_time: datetime
    status: str

    class Config:
        from_attributes = True


class QuestionCreate(BaseModel):
    match_id: str
    question_text: str
    entry_fee: int
    start_time: datetime
    end_time: datetime
    options: list[str]


class OptionResponse(BaseModel):
    id: str
    option_text: str

    class Config:
        from_attributes = True


class QuestionResponse(BaseModel):
    id: str
    match_id: str
    question_text: str
    entry_fee: int
    start_time: datetime
    end_time: datetime
    status: str
    options: list[OptionResponse]

    class Config:
        from_attributes = True


class AnswerCreate(BaseModel):
    question_id: str
    option_id: str


class AnswerResponse(BaseModel):
    id: str
    user_id: str
    question_id: str
    option_id: str

    class Config:
        from_attributes = True


class ResultCreate(BaseModel):
    question_id: str
    correct_option_id: str


class ResultResponse(BaseModel):
    id: str
    question_id: str
    correct_option_id: str
    declared_by: str
    declared_at: datetime

    class Config:
        from_attributes = True


class PointHistoryResponse(BaseModel):
    id: str
    user_id: str
    points: int
    transaction_type: str
    description: str
    created_at: datetime

    class Config:
        from_attributes = True


class NotificationResponse(BaseModel):
    id: str
    user_id: str
    title: str
    message: str
    is_read: bool
    created_at: datetime

    class Config:
        from_attributes = True


class SportUpdate(BaseModel):
    name: str


class TeamUpdate(BaseModel):
    team_name: str


class MatchUpdate(BaseModel):
    sport_id: str
    team1_id: str
    team2_id: str
    match_name: str
    start_time: datetime
    end_time: datetime


class QuestionUpdate(BaseModel):
    question_text: str
    entry_fee: int
    start_time: datetime
    end_time: datetime
    options: list[str]
