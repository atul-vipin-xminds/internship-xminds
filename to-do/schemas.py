from pydantic import BaseModel


# TAG

class TagCreate(BaseModel):
    tag_name: str


class TagResponse(BaseModel):
    id: int
    tag_name: str

    class Config:
        from_attributes = True


# TASK DETAIL

class TaskDetailCreate(BaseModel):
    description: str
    due_date: str


class TaskDetailResponse(BaseModel):
    id: int
    description: str
    due_date: str

    class Config:
        from_attributes = True


# TASK

class TaskCreate(BaseModel):
    title: str
    completed: bool = False
    user_id: int


class TaskResponse(BaseModel):
    id: int
    title: str
    completed: bool

    task_detail: TaskDetailResponse | None = None
    tags: list[TagResponse] = []

    class Config:
        from_attributes = True


# USER

class UserCreate(BaseModel):
    name: str
    username: str
    email: str
    password: str
    role: str


class UserLogin(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    tasks: list[TaskResponse] = []

    class Config:
        from_attributes = True