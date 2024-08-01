from pydantic import BaseModel, Field


class User(BaseModel):
    id: int
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
    name: str = Field(max_length=20)


class Step(BaseModel):
    id: int
    name: str = Field(max_length=20)
    group_id: int


class Issue(BaseModel):
    id: int
    name: str = Field(max_length=20)
    step_id: int
    user_id: int
    priority: str = Field(max_length=1)


project_list: list[Project] = []
