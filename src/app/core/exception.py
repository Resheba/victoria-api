from typing import Any, Literal, Self

from fastapi import Request
from fastapi.responses import JSONResponse

from .response import BaseResponse


class BaseHTTPError(Exception):
    status_code_server_error: int = 500
    status_code_client_error: int = 400

    def __init__(
        self,
        status_code: int,
        msg: str | None = None,
        data: dict[Any, Any] | None = None,
    ) -> None:
        self.status_code = status_code
        self.msg = msg
        self.data = data

    @classmethod
    async def base_exception_handler(
        cls,
        _request: Request,
        ex: Self | Exception,
    ) -> JSONResponse:
        if isinstance(ex, BaseHTTPError):
            status: Literal["success", "error", "fail"] = "success"
            if cls.status_code_client_error <= ex.status_code < cls.status_code_server_error:
                status = "error"
            elif ex.status_code >= cls.status_code_server_error:
                status = "fail"
            return JSONResponse(
                status_code=ex.status_code,
                content=BaseResponse(status=status, msg=ex.msg, data=ex.data).model_dump(
                    exclude_none=True,
                ),
            )

        return JSONResponse(
            status_code=cls.status_code_server_error,
            content=BaseResponse(status="fail", msg=str(ex), data=None).model_dump(
                exclude_none=True,
            ),
        )
