# test file for is_multiple of two numbers

import pytest
from is_multiple import is_multiple


@pytest.mark.parametrize("n, m, result", [(100, 100, 1), (100, 50, 2), (50, 10, 5)])
def test_is_multiple(n, m, result):
    ret_val = is_multiple(n, m)

    assert ret_val == result
