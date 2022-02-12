# Quick sort pytest program.

import pytest
from quick_sort import quick_sort


@pytest.mark.parametrize(
    "arr, l_idx, r_idx, result",
    [
        (
            [1, -2, -11, 10, 2, 14, 3, 7, 8, 22],
            0,
            9,
            [-11, -2, 1, 2, 3, 7, 8, 10, 14, 22],
        ),
        ([1, -2, -11, 10, 2, 14, 3], 0, 6, [-11, -2, 1, 2, 3, 10, 14]),
    ],
)
def test_quick_sort(arr, l_idx, r_idx, result):
    assert quick_sort(arr, l_idx, r_idx) == result
