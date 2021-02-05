import pytest

pytestmark = [pytest.mark.django_db]


def test_retrieve_comic(as_anon, comic):
    got = as_anon.get(f'/api/v1/comics/{comic.slug}/')

    assert got['slug'] == 'the-black-knight'
    assert got['owner']['username'] == 'arthur'


def test_list_comics(as_anon, comic):
    got = as_anon.get('/api/v1/comics/')

    assert got['results'][0]['slug'] == 'the-black-knight'
    assert got['results'][0]['owner']['username'] == 'arthur'
