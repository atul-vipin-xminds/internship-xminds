from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy import (
    select
)

from sqlalchemy.ext.asyncio import (
    AsyncSession
)

from database import (
    get_db
)

from models import (
    User
)

from schemas import (
    UserCreate,
    UserLogin,
    UserResponse,
    TokenResponse
)

from jwt_utils import (
    hash_password,
    verify_password,
    create_access_token
)

from auth import (
    get_current_user
)


router = APIRouter()


@router.post(
    "/register",
    response_model=UserResponse
)
async def register_user(
    user: UserCreate,
    db: AsyncSession = Depends(
        get_db
    )
):

    result = await db.execute(
        select(User).where(
            User.username == user.username
        )
    )

    existing_user = (
        result.scalar_one_or_none()
    )

    if existing_user:

        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    new_user = User(
        name=user.name,
        username=user.username,
        email=user.email,
        password=hash_password(
            user.password
        ),
        role="user",
        points=500
    )

    db.add(
        new_user
    )

    await db.commit()

    await db.refresh(
        new_user
    )

    return new_user


@router.post(
    "/login",
    response_model=TokenResponse
)
async def login(
    user: UserLogin,
    db: AsyncSession = Depends(
        get_db
    )
):

    result = await db.execute(
        select(User).where(
            User.username == user.username
        )
    )

    db_user = (
        result.scalar_one_or_none()
    )

    if not db_user:

        raise HTTPException(
            status_code=401,
            detail="Invalid username"
        )

    if not verify_password(
        user.password,
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


@router.get(
    "/profile",
    response_model=UserResponse
)
async def profile(
    current_user: dict = Depends(
        get_current_user
    ),
    db: AsyncSession = Depends(
        get_db
    )
):

    result = await db.execute(
        select(User).where(
            User.username ==
            current_user["sub"]
        )
    )

    user = (
        result.scalar_one_or_none()
    )

    return user