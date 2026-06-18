from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy import select

from database import get_db

from models import (
    User,
    LeaveRequest
)

from schemas import (
    LeaveCreate,
    LeaveResponse,
    LeaveStatusUpdate
)

from auth import (
    get_current_user,
    admin_required,
    employee_required
)

router = APIRouter()


@router.post(
    "/",
    response_model=LeaveResponse
)
async def apply_leave(
    leave: LeaveCreate,
    current_user: dict = Depends(
        employee_required
    ),
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(User).where(
            User.username == current_user["sub"]
        )
    )

    user = result.scalar_one_or_none()

    db_leave = LeaveRequest(
        leave_date=leave.leave_date,
        reason=leave.reason,
        status="pending",
        employee_id=user.id
    )

    db.add(db_leave)

    await db.commit()

    await db.refresh(db_leave)

    return db_leave


@router.get(
    "/my",
    response_model=list[LeaveResponse]
)
async def my_leaves(
    current_user: dict = Depends(
        employee_required
    ),
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(User).where(
            User.username == current_user["sub"]
        )
    )

    user = result.scalar_one_or_none()

    result = await db.execute(
        select(LeaveRequest).where(
            LeaveRequest.employee_id == user.id
        )
    )

    return result.scalars().all()


@router.get(
    "/",
    response_model=list[LeaveResponse]
)
async def all_leaves(
    current_user: dict = Depends(
        admin_required
    ),
    db: AsyncSession = Depends(get_db)
):

    result = await db.execute(
        select(LeaveRequest)
    )

    return result.scalars().all()


@router.post(
    "/{leave_id}/status",
    response_model=LeaveResponse
)
async def update_leave_status(
    leave_id: int,
    leave_data: LeaveStatusUpdate,
    current_user: dict = Depends(
        admin_required
    ),
    db: AsyncSession = Depends(get_db)
):

    if leave_data.status not in [
        "approved",
        "rejected"
    ]:

        raise HTTPException(
            status_code=400,
            detail="Invalid status"
        )

    result = await db.execute(
        select(LeaveRequest).where(
            LeaveRequest.id == leave_id
        )
    )

    leave = result.scalar_one_or_none()

    if not leave:

        raise HTTPException(
            status_code=404,
            detail="Leave request not found"
        )

    leave.status = leave_data.status

    await db.commit()

    await db.refresh(leave)

    return leave