from pydantic import BaseModel, Field


class StepFields:
    id: int = Field(examples=[1], title="Step ID")
    name: str = Field(max_length=20, examples=["My Step"], title="Step name")
    group_id: int = Field(examples=[15], title="Group ID")


class Step(BaseModel):
    id: int = StepFields.id
    name: str = StepFields.name
    group_id: int = StepFields.group_id


class AddStep(BaseModel):
    name: str = StepFields.name
    group_id: int = StepFields.group_id


class UpdateStep(BaseModel):
    name: str = StepFields.name
