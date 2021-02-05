import pytest

pytestmark = [pytest.mark.django_db]


def test_retrieve_user(as_anon, arthur):
    got = as_anon.get(f'/api/v1/users/{arthur.id}/')

    assert got['username'] == 'arthur'


def test_list_users(as_anon, arthur):
    got = as_anon.get('/api/v1/users/')

    assert got['results'][0]['username'] == 'arthur'
