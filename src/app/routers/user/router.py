from fastapi import APIRouter, Request

from src.app.core import BaseHTTPError, BaseResponse
from src.app.schemas import AddUser, User

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)


@router.get(
    "/{user_id}",
    response_model=BaseResponse[User],
    description="Get user by id",
    responses={404: {"description": "User not found"}},
)
async def get_user(user_id: int, request: Request) -> BaseResponse[User]:
    user_list: list[User] = request.app.state.user_list
    for user in user_list:
        if user.id == user_id:
            return BaseResponse(status="success", data=user)

    raise BaseHTTPError(status_code=404, msg="User not found")


@router.post("", response_model=BaseResponse[User], description="Add new user")
async def add_user(data: AddUser, request: Request) -> BaseResponse[User]:
    user: User = User(id=len(request.app.state.user_list) + 1, **data.model_dump())
    request.app.state.user_list.append(user)

    return BaseResponse(status="success", data=user)
