# File to test is_even script

import pytest

from is_even import is_even, Operations


@pytest.mark.parametrize(
    "num, option, result",
    [
        (10, Operations.AND, True),
        (11, Operations.AND, False),
        (2, Operations.AND, True),
        (3, Operations.AND, False),
        (10, Operations.OR, True),
        (11, Operations.OR, False),
        (2, Operations.OR, True),
        (3, Operations.OR, False),
        (10, Operations.XOR, True),
        (11, Operations.XOR, False),
        (2, Operations.XOR, True),
        (3, Operations.XOR, False),
    ],
)
def test_is_even(num, option, result):

    ret_val = is_even(num, option)

    assert ret_val == result
