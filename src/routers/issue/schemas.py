from pydantic import BaseModel, Field


class IssueFields:
    id: int = Field(examples=[37], title="Issue ID")
    name: str = Field(max_length=20, examples=["My Issue"], title="Issue name")
    step_id: int = Field(examples=[2], title="Step ID")
    user_id: int = Field(examples=[54], title="User ID")
    priority: str = Field(max_length=1, examples=["H"], title="Issue priority")
    description: str | None = Field(default=None, title="Issue description")


class Issue(BaseModel):
    id: int = IssueFields.id
    name: str = IssueFields.name
    step_id: int = IssueFields.step_id
    user_id: int = IssueFields.user_id
    priority: str = IssueFields.priority
    description: str | None = IssueFields.description


class AddIssue(BaseModel):
    name: str = IssueFields.name
    step_id: int = IssueFields.step_id
    user_id: int = IssueFields.user_id
    priority: str = IssueFields.priority
    description: str | None = IssueFields.description


class UpdateIssue(BaseModel):
    name: str = IssueFields.name
    step_id: int = IssueFields.step_id
    user_id: int = IssueFields.user_id
    priority: str = IssueFields.priority
    description: str | None = IssueFields.description
