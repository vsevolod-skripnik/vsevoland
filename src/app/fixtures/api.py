import pytest

from app.test.api_client import DRFClient


@pytest.fixture
def api():
    return DRFClient(anon=True)
