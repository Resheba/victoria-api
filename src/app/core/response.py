from typing import Generic, Literal, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class BaseResponse(BaseModel, Generic[T]):
    status: Literal["success", "error", "fail"]
    msg: str | None = None
    data: T | None = None
