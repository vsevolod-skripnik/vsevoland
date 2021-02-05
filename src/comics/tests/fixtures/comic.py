import pytest


@pytest.fixture
def comic(factory, arthur):
    defaults = {
        'slug': 'the-black-knight',
        'owner': arthur,
    }
    return factory.comic(**defaults)
