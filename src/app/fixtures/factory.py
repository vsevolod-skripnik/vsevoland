from functools import partial

import pytest
from mixer.backend.django import mixer


@pytest.fixture
def factory():
    return FixtureFactory()


def register(method):
    name = method.__name__
    FixtureRegistry.METHODS[name] = method
    return method


class FixtureRegistry:
    METHODS = {}

    def get(self, name):
        method = self.METHODS.get(name)
        if not method:
            raise AttributeError(f'Factory method “{name}” not found.')
        return method


class FixtureFactory:
    def __init__(self):
        self.mixer = mixer
        self.registry = FixtureRegistry()

    def __getattr__(self, name):
        method = self.registry.get(name)
        return partial(method, self)
