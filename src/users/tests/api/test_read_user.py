import pytest

pytestmark = [pytest.mark.django_db]


def test_retrieve_user(arthur, as_anon):
    got = as_anon.get(f'/api/v1/users/{arthur.id}/')

    assert got['username'] == 'arthur'


def test_list_users(arthur, lancelot, as_anon):
    got = as_anon.get('/api/v1/users/')

    assert got['count'] == 2
