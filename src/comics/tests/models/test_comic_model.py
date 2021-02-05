import pytest

pytestmark = [pytest.mark.django_db]


def test_str(comic):
    assert comic.__str__() == 'the-black-knight'
