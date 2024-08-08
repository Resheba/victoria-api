from collections.abc import Generator

import pytest
from fastapi.testclient import TestClient

from src.app.schemas import AddProject, Project

from .conftest import ClientPrepareTest


class PrepareTest(ClientPrepareTest):
    @pytest.fixture()
    def _project_pull(self) -> Generator[None, None, None]:
        if self.state:
            self.state.project_list.append(Project(id=1, name="test", description="test"))
            yield
            self.state.project_list.clear()
        else:
            yield


class TestProjectRouter(PrepareTest):
    expected_status_code: int = 200
    test_add_project_data: AddProject = AddProject(name="test", description="test")

    @pytest.mark.usefixtures("_project_pull")
    def test_get_project(self, client: TestClient) -> None:
        response = client.get("/project")
        assert response.status_code == TestProjectRouter.expected_status_code
        assert (
            response.json().get("data")
            == [project.model_dump() for project in self.state.project_list]
            if self.state
            else []
        )

    @staticmethod
    def test_add_project(client: TestClient) -> None:
        response = client.post(
            "/project",
            json=TestProjectRouter.test_add_project_data.model_dump(),
        )
        assert response.status_code == TestProjectRouter.expected_status_code
        assert (
            response.json().get("data")
            == Project(id=1, **TestProjectRouter.test_add_project_data.model_dump()).model_dump()
        )
