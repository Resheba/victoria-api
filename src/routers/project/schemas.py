from pydantic import BaseModel, Field


class ProjectFields:
    id: int = Field(examples=[341], title="Project ID")
    name: str = Field(max_length=20, examples=["My Project"], title="Project name")
    description: str | None = Field(default=None, title="Project description")


class Project(BaseModel):
    id: int = ProjectFields.id
    name: str = ProjectFields.name
    description: str | None = ProjectFields.description


class AddProject(BaseModel):
    name: str = ProjectFields.name
    description: str | None = ProjectFields.description


class UpdateProject(BaseModel):
    name: str = ProjectFields.name
    description: str | None = ProjectFields.description
