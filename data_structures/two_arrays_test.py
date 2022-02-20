# pytest script for Two Arrays program.

import pytest
from two_arrays import two_arrays


@pytest.mark.parametrize(
    "arr1, arr2, target, result",
    [
        ([2, 5, 7, 8], [8, 5, 7, 1], 13, (2, 8)),
        ([2, 5, 7, 8], [8, 5, 7, 1], 11, (5, 8)),
    ],
)
def test_two_arrays(arr1, arr2, target, result):
    assert two_arrays(arr1, arr2, target) == result
