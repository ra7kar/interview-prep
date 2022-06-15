# pytest script for Min Heap

import pytest
from heap import MinHeap


@pytest.mark.parametrize(
    "arr, result",
    [
        ([50, 10, 45, 20, 30, 60, 22, 32, 12, 5], [10, 12, 22, 20, 30, 60, 45, 50, 32]),
        ([4, 12, 22, 20, 30, 60, 45, 50, 32], [12, 20, 22, 32, 30, 60, 45, 50]),
    ],
)
def test_heap(arr, result):
    heap = MinHeap(arr)
    heap.pop()
    assert heap.get_heap() == result
