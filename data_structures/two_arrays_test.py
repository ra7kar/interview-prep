# pytest script for two_arrays program.

import pytest
from two_arrays import two_arrays


@pytest.mark.parametrize(
    "arr1, arr2, target, result",
    [
        ([2, 5, 7, 8], [4, 5, 8, 7], 11, (2, 8)),
        ([2, 5, 7, 8], [8, 5, 7, 1], 13, (5, 8)),
    ],
)
def test_two_arrays(arr1, arr2, target, result):
    assert two_arrays(arr1, arr2, target) == result
