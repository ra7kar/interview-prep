# pytest script for sherlock squares, hacker rank problem.

import pytest
from sherlock_squares import squares_1


@pytest.mark.parametrize(
    "a, b , result",
    [
        (3, 9, 2),
        (17, 24, 0),
        (17, 25, 1),
    ],
)
def test_sherlock_squares(a, b, result):
    assert squares_1(a, b) == result
