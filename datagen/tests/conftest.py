import pytest
from src.utils.wait_for_service import wait_for_openrefine

@pytest.fixture(scope="session", autouse=True)
def wait_for_openrefine_service():
    wait_for_openrefine()