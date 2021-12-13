# test file for generator.py

import pytest

from generator import factor


@pytest.mark.parametrize(
    "num, result",
    [
        (10, [1, 2, 5, 10]),
        (100, [1, 2, 4, 5, 10, 20, 25, 50, 100]),
    ],
)
def test_generator(num, result):
    ret_val = factor(num)
    assert ret_val == result
