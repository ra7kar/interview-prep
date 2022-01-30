# subarray division: pytest script

import pytest
from subarray_division import birthday


@pytest.mark.parametrize(
    "s, d, m, result",
    [
        ([1, 2, 1, 3, 2], 3, 2, 2),
        ([1, 1, 1, 1, 1, 1], 3, 2, 0),
        ([4], 4, 1, 1),
    ],
)
def test_birthday(s, d, m, result):
    assert birthday(s, d, m) == result
