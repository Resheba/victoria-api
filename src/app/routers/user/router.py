from app.core import BaseHTTPError, BaseResponse
from app.schemas import AddUser, User, user_list
from fastapi import APIRouter

router = APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404: {"description": "Not found"}},
)


@router.get("/get_users", response_model=BaseResponse[list[User]], description="Get all users")
async def get_users() -> BaseResponse[list[User]]:
    return BaseResponse(status="success", msg="Users received", data=user_list)


@router.get(
    "/get_user{user_id}",
    response_model=BaseResponse[User],
    description="Get user by id",
    responses={404: {"description": "User not found"}},
)
async def get_user(user_id: int) -> BaseResponse[User]:
    for user in user_list:
        if user.id == user_id:
            return BaseResponse(status="success", msg="User received", data=user)

    raise BaseHTTPError(status_code=404, msg="User not found")


@router.post("/add_user", response_model=BaseResponse[User], description="Add new user")
async def add_user(data: AddUser) -> BaseResponse[User]:
    user: User = User(id=len(user_list) + 1, **data.model_dump())
    user_list.append(user)

    return BaseResponse(status="success", msg="User added", data=user)
