from fastapi import APIRouter, Request

from src.app.core import BaseHTTPError, BaseResponse
from src.app.schemas import AddIssue, Issue, UpdateIssue

router = APIRouter(
    prefix="/issue",
    tags=["issue"],
    responses={404: {"description": "Not found"}},
)


@router.get(
    "",
    response_model=BaseResponse[list[Issue]],
    description="Get issues by user or step",
    responses={404: {"description": "Issues not found"}},
)
async def get_issues_by_user(
    request: Request,
    user_id: int | None = None,
    step_id: int | None = None,
) -> BaseResponse[list[Issue]]:
    issue_list: list[Issue] = request.app.state.issue_list
    data: list[Issue] = [
        issue for issue in issue_list if issue.user_id == user_id or issue.step_id == step_id
    ]
    if data:
        return BaseResponse(status="success", data=data)
    raise BaseHTTPError(status_code=404, msg="Issues not found")


@router.post(
    "",
    response_model=BaseResponse[Issue],
    description="Add new issue",
    responses={
        404: {"description": "User or step not found"},
    },
)
async def add_issue(data: AddIssue, request: Request) -> BaseResponse[Issue]:
    if data.user_id not in [user.id for user in request.app.state.user_list]:
        raise BaseHTTPError(status_code=404, msg="User not found")

    if data.step_id not in [step.id for step in request.app.state.step_list]:
        raise BaseHTTPError(status_code=404, msg="Step not found")

    issue: Issue = Issue(id=len(request.app.state.issue_list) + 1, **data.model_dump())
    request.app.state.issue_list.append(issue)

    return BaseResponse(status="success", data=issue)


@router.patch(
    "/{issue_id}",
    response_model=BaseResponse[Issue],
    description="Update issue",
    responses={404: {"description": "Issue not found"}},
)
async def update_issue(data: UpdateIssue, issue_id: int, request: Request) -> BaseResponse[Issue]:
    issue_list: list[Issue] = request.app.state.issue_list
    for issue in issue_list:
        if issue.id == issue_id:
            for key, value in data.model_dump(exclude_none=True).items():
                setattr(issue, key, value)

            return BaseResponse(status="success", data=issue)

    raise BaseHTTPError(status_code=404, msg="Issue not found")


@router.delete(
    "/{issue_id}",
    description="Delete issue",
    responses={404: {"description": "Issue not found"}},
)
async def delete_issue(issue_id: int, request: Request) -> BaseResponse[Issue]:
    issue_list: list[Issue] = request.app.state.issue_list
    for issue in issue_list:
        if issue.id == issue_id:
            issue_list.remove(issue)
            return BaseResponse(status="success", data=issue)

    raise BaseHTTPError(status_code=404, msg="Issue not found")
