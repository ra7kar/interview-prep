# Bubble sort: pytest script.

import pytest
from bubble_sort import bubble_sort


@pytest.mark.parametrize(
    "arr, result",
    [
        ([9, 4, 2, 5, 7, 1, 8, 3, 0], [0, 1, 2, 3, 4, 5, 7, 8, 9]),
        ([4, 7, 1, 8, 3], [1, 3, 4, 7, 8]),
    ],
)
def test_bubble_sort(arr, result):
    assert bubble_sort(arr) == result
