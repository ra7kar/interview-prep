# pytest for magic_square2.
# hacker rank problem

import pytest
from magic_square2 import magic_square


@pytest.mark.parametrize(
    "s, result",
    [
        ([[4, 8, 2], [4, 5, 7], [6, 1, 6]], 4),
        ([[4, 9, 2], [3, 5, 7], [8, 1, 5]], 1),
    ],
)
def test_magic_square2(s, result):
    assert magic_square(s) == result
