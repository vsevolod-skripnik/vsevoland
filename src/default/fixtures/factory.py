import pytest

from default.testing.factory import FixtureFactory


@pytest.fixture
def factory():
    return FixtureFactory()
