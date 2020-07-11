import pytest
from mixer.backend.django import mixer


@pytest.fixture
def page_factory():
    def _create_page(**kwargs):
        defaults = {
            'title': 'Test page',
            'slug': 'test-page',
            'content': '<p>Test content</p>',
            **kwargs,
        }
        return mixer.blend('pages.Page', **defaults)
    return _create_page


@pytest.fixture
def page(page_factory):
    return page_factory()
