from fastapi import APIRouter, Request

from src.app.core import BaseHTTPError, BaseResponse
from src.app.schemas import AddStep, Step, UpdateStep

router = APIRouter(
    prefix="/step",
    tags=["step"],
    responses={404: {"description": "Not found"}},
)


@router.post(
    "",
    response_model=BaseResponse[Step],
    description="Add new step",
    responses={404: {"description": "Group not found"}},
)
async def add_step(data: AddStep, request: Request) -> BaseResponse[Step]:
    if data.group_id in [group.id for group in request.app.state.group_list]:
        step: Step = Step(id=len(request.app.state.step_list) + 1, **data.model_dump())
        request.app.state.step_list.append(step)
        return BaseResponse(status="success", data=step)

    raise BaseHTTPError(status_code=404, msg="Group not found")


@router.get(
    "/{group_id}",
    response_model=BaseResponse[Step],
    description="Get step by id",
    responses={404: {"description": "Group not found"}},
)
async def get_steps(group_id: int, request: Request) -> BaseResponse[Step]:
    for step in request.app.state.step_list:
        if step.group_id == group_id:
            return BaseResponse(status="success", data=step)

    raise BaseHTTPError(status_code=404, msg="Group not found")


@router.patch(
    "/{step_id}",
    response_model=BaseResponse[Step],
    description="Update step",
    responses={404: {"description": "Step not found"}},
)
async def update_step(data: UpdateStep, step_id: int, request: Request) -> BaseResponse[Step]:
    step_list: list[Step] = request.app.state.step_list
    for step in step_list:
        if step.id == step_id:
            step.name = data.name
            return BaseResponse(status="success", data=step)

    raise BaseHTTPError(status_code=404, msg="Step not found")


@router.delete(
    "/{step_id}",
    response_model=BaseResponse[Step],
    description="Delete step",
    responses={404: {"description": "Step not found"}},
)
async def delete_step(step_id: int, request: Request) -> BaseResponse[Step]:
    step_list: list[Step] = request.app.state.step_list
    for step in step_list:
        if step.id == step_id:
            step_list.remove(step)
            return BaseResponse(status="success", data=step)

    raise BaseHTTPError(status_code=404, msg="Step not found")
