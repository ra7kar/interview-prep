# pytest for beautiful days, hacker rank problem.

import pytest
from beautiful_days import beautiful_days


@pytest.mark.parametrize(
    "i, j, k, result",
    [
        (20, 23, 6, 2),
        (13, 45, 3, 33),
    ],
)
def test_beautiful_days(i, j, k, result):
    assert beautiful_days(i, j, k)
