import pytest

from default.testing import ApiClient


@pytest.fixture
def as_anon():
    return ApiClient()
