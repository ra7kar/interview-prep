# test for abs of diag sum of an array

import pytest
import diagonal_sum


@pytest.mark.parametrize(
    "l_list, result",
    [
        ([[11, 2, 4], [4, 5, 6], [10, 8, -10]], 13),
        ([[11, 2, 4], [4, 5, 6], [10, 8, -12]], 15),
    ],
)
def test_diagonal_sum(l_list, result):
    ret_val = diagonal_sum.diagonal_sum(l_list)
    assert ret_val == result
