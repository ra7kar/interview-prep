# pytest script for Cut Sticks, hacker rank problem.

import pytest
from cut_sticks import cut_the_stick


@pytest.mark.parametrize(
    "arr, result",
    [
        ([1, 2, 3, 4, 3, 3, 2, 1], [8, 6, 4, 1]),
        ([5, 4, 4, 2, 2, 8], [6, 4, 2, 1]),
    ],
)
def test_cut_the_sticks(arr, result):
    assert cut_the_stick(arr) == result
