# test file for is_multiple of two numbers

import pytest
from is_multiple import is_multiple


@pytest.mark.parametrize(
    "n, m, result", [(100, 100, True), (100, 50, True), (50, 10, True), (100, 9, False)]
)
def test_is_multiple(n, m, result):
    ret_val = is_multiple(n, m)

    assert ret_val == result
