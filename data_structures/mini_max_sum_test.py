# pytest for mini_max_sum

import pytest
from mini_max_sum import min_max_sum


@pytest.mark.parametrize(
    "py_list, result",
    [
        ([1, 3, 5, 7, 9, 10, 11], (35, 45)),
        ([7, 69, 2, 221, 8974], (299, 9271)),
    ],
)
def test_mini_max_sum(py_list, result):
    ret_val = min_max_sum(py_list)

    assert ret_val == result
