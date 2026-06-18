from fastapi import (
    Depends,
    HTTPException
)

from fastapi.security import (
    OAuth2PasswordBearer
)

from jwt_utils import verify_token


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/users/login"
)


def get_current_user(
    token: str = Depends(oauth2_scheme)
):

    payload = verify_token(token)

    if payload is None:

        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    return payload


def admin_required(
    current_user: dict = Depends(
        get_current_user
    )
):

    if current_user["role"] != "admin":

        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )

    return current_user


def employee_required(
    current_user: dict = Depends(
        get_current_user
    )
):

    if current_user["role"] != "employee":

        raise HTTPException(
            status_code=403,
            detail="Access denied"
        )

    return current_user