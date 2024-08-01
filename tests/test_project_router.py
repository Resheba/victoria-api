from fastapi.testclient import TestClient


class TestProjectRouter:
    @staticmethod
    def test_get_project(client: TestClient) -> None:
        response = client.get("/project/get_projects")
        expected_status_code = 200
        assert response.status_code == expected_status_code
