import asyncio
from collections import abc
from functools import wraps
from typing import Any, cast

from pydantic import BaseModel
from sqlalchemy.orm import DeclarativeBase


class SerializatorDTO:
    def __init__(self, _to: type[BaseModel]) -> None:
        self._to = _to

    @staticmethod
    def from_orm(
        _from: abc.Sequence[DeclarativeBase] | DeclarativeBase | None,
        _to: type[BaseModel],
    ) -> abc.Sequence[BaseModel] | BaseModel | None:
        if _from is None:
            return _from
        if issubclass(type(_from), abc.Sequence):
            return tuple(
                _to.model_validate(fr, from_attributes=True)
                for fr in cast(abc.Sequence[DeclarativeBase], _from)
            )
        return _to.model_validate(_from, from_attributes=True)

    def __call__(
        self,
        func: abc.Callable[..., Any],
    ) -> abc.Callable[..., abc.Coroutine[Any, Any, abc.Sequence[BaseModel] | BaseModel | None]]:
        @wraps(func)
        async def wrapper(*args: Any, **kwargs: Any) -> abc.Sequence[BaseModel] | BaseModel | None:
            if asyncio.iscoroutinefunction(func):
                result = await func(*args, **kwargs)
            else:
                result = func(*args, **kwargs)
            return self.from_orm(result, self._to)

        return wrapper
