from pydantic import BaseModel, Field


class User(BaseModel):
    id: int
    tg_teg: str = Field(max_length=32)


class AddUser(BaseModel):
    tg_teg: str = Field(max_length=32)


class Project(BaseModel):
    id: int
    name: str = Field(max_length=20)
    description: str | None = None


class AddProject(BaseModel):
    name: str = Field(max_length=20)
    description: str | None = None


class UpdateProject(BaseModel):
    name: str = Field(max_length=20)
    description: str | None = None


class Group(BaseModel):
    id: int
    prject_id: int
    name: str = Field(max_length=20)


class AddGroup(BaseModel):
    name: str = Field(max_length=20)
    prject_id: int


class UpdateGroup(BaseModel):
    name: str = Field(max_length=20)


class Step(BaseModel):
    id: int
    name: str = Field(max_length=20)
    group_id: int


class AddStep(BaseModel):
    name: str = Field(max_length=20)
    group_id: int


class UpdateStep(BaseModel):
    name: str = Field(max_length=20)


class Issue(BaseModel):
    id: int
    name: str = Field(max_length=20)
    step_id: int
    user_id: int
    priority: str = Field(max_length=1)
    description: str | None = None


class AddIssue(BaseModel):
    name: str = Field(max_length=20)
    step_id: int
    user_id: int
    priority: str = Field(max_length=1)
    description: str | None = None


class UpdateIssue(BaseModel):
    name: str = Field(max_length=20)
    step_id: int
    user_id: int
    priority: str = Field(max_length=1)
    description: str | None = None
