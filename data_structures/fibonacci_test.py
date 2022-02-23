# pytest script for fibonacci program

import pytest

from fibonacci import fib_seq


@pytest.mark.parametrize(
    "n, result",
    [
        (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]),
        (5, [0, 1, 1, 2, 3]),
    ],
)
def test_fib_seq(n, result):
    assert fib_seq(n) == result
