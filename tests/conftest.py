import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from starlette.datastructures import State

from src.app import app


class ClientPrepareTest:
    _app: FastAPI = app()
    application = TestClient(
        _app,
    )
    state: State | None = getattr(application.app, "state", None)

    @pytest.fixture()
    def client(self) -> TestClient:
        return self.application
