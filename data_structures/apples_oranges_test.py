# pytest for apples_oranges

import pytest
from apples_oranges import countApplesAndOranges


@pytest.mark.parametrize(
    "s, t, a, b, apples, oranges, result",
    [
        (7, 10, 4, 12, [2, 3, -4], [3, -2, -4], (1, 2)),
        (7, 11, 5, 15, [-2, 2, 1], [5, -6], (1, 1)),
    ],
)
def test_apples_oranges(s, t, a, b, apples, oranges, result):

    assert countApplesAndOranges(s, t, a, b, apples, oranges) == result
