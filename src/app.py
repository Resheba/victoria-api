from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import APIRouter, FastAPI
from loguru import logger

from .core import BaseHTTPError
from .routers import group_router, issue_router, project_router, step_router, user_router

# from src.database import db_manager


@asynccontextmanager
async def lifespan(_app: FastAPI) -> AsyncGenerator[None, None]:
    # await db_manager.connect(create_all=True, expire_on_commit=False)
    logger.debug("Start")
    yield
    logger.debug("End")


def app() -> FastAPI:
    from . import __version__ as version

    app: FastAPI = FastAPI(
        title="Vicrotia API",
        version=".".join(str(v) for v in version),
        root_path="/api",
        lifespan=lifespan,
        exception_handlers={Exception: BaseHTTPError.base_exception_handler},
    )
    v1_router: APIRouter = APIRouter(prefix="/v1")
    v1_router.include_router(project_router)
    v1_router.include_router(user_router)
    v1_router.include_router(group_router)
    v1_router.include_router(step_router)
    v1_router.include_router(issue_router)

    app.include_router(v1_router)

    for state_var in (
        "project_list",
        "user_list",
        "group_list",
        "step_list",
        "issue_list",
    ):
        setattr(app.state, state_var, [])

    return app
