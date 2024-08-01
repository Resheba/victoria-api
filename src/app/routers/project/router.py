from app.core import BaseHTTPError, BaseResponse
from app.schemas import AddProject, Project, UpdateProject, project_list
from fastapi import APIRouter

router = APIRouter(
    prefix="/project",
    tags=["project"],
    responses={404: {"description": "Not found"}},
)


@router.post("/add_project", response_model=BaseResponse[Project])
async def add_project(data: AddProject) -> BaseResponse[Project]:
    project: Project = Project(id=len(project_list) + 1, **data.model_dump())
    project_list.append(project)

    return BaseResponse(status="success", msg="Project added", data=project)


@router.get("/get_projects", response_model=BaseResponse[list[Project]])
async def get_projects() -> BaseResponse[list[Project]]:
    return BaseResponse(status="success", msg="Projects received", data=project_list)


@router.patch("/update_project{project_id}", response_model=BaseResponse[Project])
async def update_project(data: UpdateProject, project_id: int) -> BaseResponse[Project]:
    for project in project_list:
        if project.id == project_id:
            project.name = data.name
            project.description = data.description
            return BaseResponse(status="success", msg="Project updated", data=project)

    raise BaseHTTPError(status_code=404, msg="Project not found")


@router.delete("/delete_project{project_id}", response_model=BaseResponse[Project])
async def delete_project(project_id: int) -> BaseResponse[Project]:
    for project in project_list:
        if project.id == project_id:
            project_list.remove(project)
            return BaseResponse(status="success", msg="Project deleted", data=project)

    raise BaseHTTPError(status_code=404, msg="Project not found")
