from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from loguru import logger

from .core import BaseHTTPError, base_exception_handler
from .routers import group_router, project_router, user_router

# from src.database import db_manager


def app() -> FastAPI:
    @asynccontextmanager
    async def lifespan(_app: FastAPI) -> AsyncGenerator[None, None]:
        # await db_manager.connect(create_all=True, expire_on_commit=False)
        logger.debug("Start")
        yield
        logger.debug("End")

    app: FastAPI = FastAPI(
        lifespan=lifespan,
        exception_handlers={BaseHTTPError: base_exception_handler},
    )
    app.include_router(project_router)
    app.include_router(user_router)
    app.include_router(group_router)
    app.state.project_list = []

    return app
