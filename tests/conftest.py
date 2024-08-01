import sys
from pathlib import Path

sys.path.insert(0, Path(Path(Path(__file__).parent / ".." / "src")).resolve().as_posix())

import pytest
from fastapi.testclient import TestClient

from src.app.app import app


@pytest.fixture()
def client() -> TestClient:
    return TestClient(app())
