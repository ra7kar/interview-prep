# pytest for find digits, Hacker rank problem.

import pytest
from find_digits import find_digits


@pytest.mark.parametrize(
    "n, result",
    [
        (10, 1),
        (124, 3),
        (1110, 3),
    ],
)
def test_find_digits(n, result):
    assert find_digits(n) == result
