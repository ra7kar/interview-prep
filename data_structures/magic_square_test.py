# pytest script for magic_square, Hacker rank problem.

import pytest
from magic_square import magic_square


@pytest.mark.parametrize(
    "s, result",
    [
        ([[5, 3, 4], [1, 5, 8], [6, 4, 2]], 7),
        ([[4, 9, 2], [3, 5, 7], [8, 1, 5]], 1),
        ([[4, 8, 2], [4, 5, 7], [6, 1, 6]], 4),
    ],
)
def test_magic_square(s, result):
    assert magic_square(s) == result
