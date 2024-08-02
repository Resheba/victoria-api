import pytest
from fastapi.testclient import TestClient
from starlette.datastructures import State

from src.app.app import app


class ClientPrepareTest:
    application = TestClient(app())
    state: State | None = getattr(application.app, "state", None)

    @pytest.fixture()
    def client(self) -> TestClient:
        return self.application
