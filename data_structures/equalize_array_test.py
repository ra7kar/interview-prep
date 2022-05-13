# pytest script for equalize array , hacker rank problem.

import pytest
from equalize_array import equalize_arr


@pytest.mark.parametrize(
    "arr, result",
    [
        ([3, 3, 2, 1, 3], 2),
        ([1, 2, 3, 1, 2, 3, 3, 3, 9], 5),
        ([1, 2, 3, 1, 2, 3, 3, 3], 4),
    ],
)
def test_equalize_array(arr, result):
    equalize_arr
