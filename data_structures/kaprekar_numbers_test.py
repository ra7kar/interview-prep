# pytest script for kaprekar numbers, hacker rank problem.

import pytest
from kaprekar_numbers import kaprekar_numbers


@pytest.mark.parametrize(
    "p, q, result",
    [
        (1, 700, "1 9 45 55 99 297"),
        (300, 700, "INVALID RANGE"),
    ],
)
def test_kaprekar_numbers(p, q, result):
    assert kaprekar_numbers(p, q) == result
