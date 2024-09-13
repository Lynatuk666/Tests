import pytest
import main as m

@pytest.mark.parametrize(
    "data, expected",
    (
        ((1, 8, 15), "-3.0 -5.0"),
        ((1, -13, 12), "12.0 1.0"),
        ((-4, 28, -49), "3.5"),
        ((1, 1, 1), "корней нет")
    )
)
def test_quadratic(data, expected):
    assert m.solution(*data) == expected


if __name__ == '__main__':
    test_quadratic()
