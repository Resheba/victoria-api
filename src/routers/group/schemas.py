from pydantic import BaseModel, Field


class GroupFields:
    id: int = Field(examples=[15], title="Group ID")
    prject_id: int = Field(examples=[341], title="Project ID")
    name: str = Field(max_length=20, examples=["Andry's group"], title="Group name")


class Group(BaseModel):
    id: int = GroupFields.id
    prject_id: int = GroupFields.prject_id
    name: str = GroupFields.name


class AddGroup(BaseModel):
    name: str = GroupFields.name
    prject_id: int = GroupFields.prject_id


class UpdateGroup(BaseModel):
    name: str = GroupFields.name
