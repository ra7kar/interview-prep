# pytest for min_heap_sort program.

import pytest

from min_heap_sort import MinHeap


@pytest.mark.parametrize(
    "l, result",
    [
        ([4, 5, 6, 7, 1, 2, 3], [1, 2, 3, 4, 5, 6, 7]),
        ([3, 5, 7, 1, 5, 8, 2, 1], [1, 1, 2, 3, 5, 5, 7, 8]),
    ],
)
def test_min_heap_sort(py_list, result):
    sorted_list = []
    min_heap = MinHeap(py_list)
    assert min_heap.sorted_list(sorted_list) == result
