import pytest


@pytest.fixture
def anon(factory):
    return factory.anon()


@pytest.fixture
def arthur(factory):
    defaults = {'username': 'arthur'}
    return factory.user(**defaults)


@pytest.fixture
def lancelot(factory):
    defaults = {'username': 'lancelot'}
    return factory.user(**defaults)
