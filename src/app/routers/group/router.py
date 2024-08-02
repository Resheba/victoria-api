from app.core import BaseHTTPError, BaseResponse
from app.schemas import AddGroup, Group, UpdateGroup, group_list
from fastapi import APIRouter

router = APIRouter(
    prefix="/group",
    tags=["group"],
    responses={404: {"description": "Not found"}},
)


@router.post("/add_group", response_model=BaseResponse[Group], description="Add new group")
async def add_group(data: AddGroup) -> BaseResponse[Group]:
    group: Group = Group(id=len(group_list) + 1, **data.model_dump())
    group_list.append(group)

    return BaseResponse(status="success", msg="Group added", data=group)


@router.patch(
    "/update_group{group_id}",
    response_model=BaseResponse[Group],
    description="Update group",
    responses={404: {"description": "Group not found"}},
)
async def update_group(data: UpdateGroup, group_id: int) -> BaseResponse[Group]:
    for group in group_list:
        if group.id == group_id:
            group.name = data.name
            group.description = data.description
            return BaseResponse(status="success", msg="Group updated", data=group)

    raise BaseHTTPError(status_code=404, msg="Group not found")


@router.delete(
    "/delete_group{group_id}",
    response_model=BaseResponse[Group],
    description="Delete group",
    responses={404: {"description": "Group not found"}},
)
async def delete_group(group_id: int) -> BaseResponse[Group]:
    for group in group_list:
        if group.id == group_id:
            group_list.remove(group)
            return BaseResponse(status="success", msg="Group deleted", data=group)

    raise BaseHTTPError(status_code=404, msg="Group not found")


@router.get(
    "/get_groups{project_id}",
    response_model=BaseResponse[list[Group]],
    description="Get all groups",
    responses={404: {"description": "Groups not found"}},
)
async def get_groups(project_id: int) -> BaseResponse[list[Group]]:
    for group in group_list:
        if group.prject_id == project_id:
            return BaseResponse(status="success", msg="Groups received", data=group_list)

    raise BaseHTTPError(status_code=404, msg="Groups not found")
