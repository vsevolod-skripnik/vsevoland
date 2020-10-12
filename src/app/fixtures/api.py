import pytest

from app.testing import ApiClient


@pytest.fixture
def as_anon():
    return ApiClient()
