from pydantic import BaseModel, Field


class UserFields:
    id: int = Field(examples=[45], title="User ID")
    tg_teg: str = Field(max_length=32, examples=["@Andry"], title="Telegram username tag")


class User(BaseModel):
    id: int = UserFields.id
    tg_teg: str = UserFields.tg_teg


class AddUser(BaseModel):
    tg_teg: str = UserFields.tg_teg
