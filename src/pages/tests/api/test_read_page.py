import pytest

pytestmark = [pytest.mark.django_db]


def test_read_page(api, page):
    got = api.get(f'/api/v1/pages/{page.id}/')

    assert got['title'] == 'Test page'
    assert got['slug'] == 'test-page'
    assert got['content'] == '<p>Test content</p>'


def test_list_pages(api, page):
    got = api.get('/api/v1/pages/')

    assert got['results'][0]['title'] == 'Test page'
    assert got['results'][0]['slug'] == 'test-page'
    assert got['results'][0]['content'] == '<p>Test content</p>'
