# pytest script for hurdle_race , hacker rank problem.

import pytest
from hurdle_race import hurdle_race


@pytest.mark.parametrize(
    "k, height, result",
    [
        (1, [2, 5, 4, 5, 2], 4),
        (7, [2, 5, 4, 5, 2], 0),
    ],
)
def test_hurdle_race(k, height, result):
    assert hurdle_race(k, height) == result
