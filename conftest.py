import pytest
from core.client import get_client

@pytest.fixture(scope="session")
def client():
    return get_client()