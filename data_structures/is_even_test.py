# File to test is_even script

import pytest

from is_even import is_even


@pytest.mark.parametrize(
    "num, option, result",
    [
        (10, "AND", True),
        (11, "AND", False),
        (2, "AND", True),
        (3, "AND", False),
        (10, "OR", True),
        (11, "OR", False),
        (2, "OR", True),
        (3, "OR", False),
        (10, "XOR", True),
        (11, "XOR", False),
        (2, "XOR", True),
        (3, "XOR", False),
    ],
)
def test_is_even(num, option, result):
    ret_val = is_even(num, option)

    assert ret_val == result
