import pytest

@pytest.mark.parametrize(
    "a,b,expected",
    [
        (1, 2, 3),
        (5, 5, 10),
        (10, -5, 5),
        (0, 0, 0)
    ]
)
def test_addition(a, b, expected):
    assert a + b == expected

@pytest.mark.smoke
def test_simple_add():
    assert 1 + 1 == 2



