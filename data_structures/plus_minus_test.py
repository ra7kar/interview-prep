# plus_minus test program.

import pytest
from plus_minus import plus_minus


@pytest.mark.parametrize(
    "py_list, result",
    [
        ([1, 1, 0, -1, -1], ["0.400000", "0.400000", "0.200000"]),
        ([-4, 3, -9, 0, 4, 1], ["0.500000", "0.333333", "0.166667"]),
    ],
)
def test_plus_minus(py_list, result):
    ret_val = plus_minus(py_list)

    assert ret_val == result
