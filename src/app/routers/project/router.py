from fastapi import APIRouter, Request

from src.app.core import BaseHTTPError, BaseResponse
from src.app.schemas import AddProject, Project, UpdateProject

router = APIRouter(
    prefix="/project",
    tags=["project"],
    responses={404: {"description": "Not found"}},
)


@router.post(
    "",
    response_model=BaseResponse[Project],
    description="Add new project",
    responses={404: {"description": "Project not found"}},
)
async def add_project(data: AddProject, request: Request) -> BaseResponse[Project]:
    project: Project = Project(id=len(request.app.state.project_list) + 1, **data.model_dump())
    request.app.state.project_list.append(project)

    return BaseResponse(status="success", data=project)


@router.get(
    "",
    response_model=BaseResponse[list[Project]],
    description="Get all projects",
    responses={404: {"description": "Projects not found"}},
)
async def get_projects(request: Request) -> BaseResponse[list[Project]]:
    return BaseResponse(
        status="success",
        data=request.app.state.project_list,
    )


@router.patch(
    "/{project_id}",
    response_model=BaseResponse[Project],
    description="Update project",
    responses={404: {"description": "Project not found"}},
)
async def update_project(
    data: UpdateProject,
    project_id: int,
    request: Request,
) -> BaseResponse[Project]:
    project_list: list[Project] = request.app.state.project_list
    for project in project_list:
        if project.id == project_id:
            project.name = data.name
            project.description = data.description
            return BaseResponse(status="success", data=project)

    raise BaseHTTPError(status_code=404, msg="Project not found")


@router.delete(
    "/{project_id}",
    response_model=BaseResponse[Project],
    description="Delete project",
    responses={404: {"description": "Project not found"}},
)
async def delete_project(project_id: int, request: Request) -> BaseResponse[Project]:
    project_list: list[Project] = request.app.state.project_list
    for project in project_list:
        if project.id == project_id:
            project_list.remove(project)
            return BaseResponse(status="success", data=project)

    raise BaseHTTPError(status_code=404, msg="Project not found")
