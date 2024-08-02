from fastapi import APIRouter, Request

from src.app.core import BaseHTTPError, BaseResponse
from src.app.schemas import AddGroup, Group, UpdateGroup

router = APIRouter(
    prefix="/group",
    tags=["group"],
    responses={404: {"description": "Not found"}},
)


@router.post("", response_model=BaseResponse[Group], description="Add new group")
async def add_group(data: AddGroup, request: Request) -> BaseResponse[Group]:
    if data.prject_id in [project.id for project in request.app.state.project_list]:
        group: Group = Group(id=len(request.app.state.group_list) + 1, **data.model_dump())
        request.app.state.group_list.append(group)

    else:
        raise BaseHTTPError(status_code=404, msg="Project not found")

    return BaseResponse(status="success", data=group)


@router.patch(
    "/{group_id}",
    response_model=BaseResponse[Group],
    description="Update group",
    responses={404: {"description": "Group not found"}},
)
async def update_group(data: UpdateGroup, group_id: int, request: Request) -> BaseResponse[Group]:
    group_list: list[Group] = request.app.state.group_list
    for group in group_list:
        if group.id == group_id:
            group.name = data.name
            return BaseResponse(status="success", data=group)

    raise BaseHTTPError(status_code=404, msg="Group not found")


@router.delete(
    "/{group_id}",
    response_model=BaseResponse[Group],
    description="Delete group",
    responses={404: {"description": "Group not found"}},
)
async def delete_group(group_id: int, request: Request) -> BaseResponse[Group]:
    group_list: list[Group] = request.app.state.group_list
    for group in group_list:
        if group.id == group_id:
            group_list.remove(group)
            return BaseResponse(status="success", data=group)

    raise BaseHTTPError(status_code=404, msg="Group not found")


@router.get(
    "",
    response_model=BaseResponse[list[Group]],
    description="Get all groups",
    responses={404: {"description": "Groups not found"}},
)
async def get_groups(project_id: int, request: Request) -> BaseResponse[list[Group]]:
    group_list: list[Group] = request.app.state.group_list
    for group in group_list:
        if group.prject_id == project_id:
            return BaseResponse(status="success", data=group_list)

    raise BaseHTTPError(status_code=404, msg="Groups not found")
