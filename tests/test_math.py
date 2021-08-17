import pytest


def test_addition():
	assert 1 + 1 == 2

@pytest.mark.parametrize("a, b, expected", [(2, 2, 4), (3, 9, 27), (5, 4, 20), (3, 1, 3)])
def test_multiplication(a, b, expected):
	assert a * b == expected