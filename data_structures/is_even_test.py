# File to test is_even script

import pytest

from is_even import is_even


@pytest.mark.parametrize(
    "num, result",
    [
        (10, True),
        (11, False),
        (2, True),
        (3, False),
    ],
)
def test_is_even(num, result):
    ret_val = is_even(num)

    assert ret_val == result
