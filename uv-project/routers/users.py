from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from fastapi.security import (
    OAuth2PasswordRequestForm
)

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import get_db

from models import User

from schemas import (
    UserCreate,
    UserResponse,
    TokenResponse
)

from jwt_utils import (
    hash_password,
    verify_password,
    create_access_token
)

router = APIRouter()


@router.post(
    "/register",
    response_model=UserResponse
)
async def register_user(
    user: UserCreate,
    db: AsyncSession = Depends(get_db)
):
    # existing register code
    ...


@router.post(
    "/login",
    response_model=TokenResponse
)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(User).where(
            User.username == form_data.username
        )
    )

    db_user = result.scalar_one_or_none()

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid username"
        )

    if not verify_password(
        form_data.password,
        db_user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )

    token = create_access_token(
        {
            "sub": db_user.username,
            "role": db_user.role
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }