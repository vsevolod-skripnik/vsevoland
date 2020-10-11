import pytest

pytestmark = [pytest.mark.django_db]


def test_retrieve_user(arthur, api):
    got = api.get(f'/api/v1/users/{arthur.id}/')

    assert got['username'] == 'arthur'


def test_list_users(arthur, lancelot, api):
    got = api.get('/api/v1/users/')

    assert got['count'] == 2
