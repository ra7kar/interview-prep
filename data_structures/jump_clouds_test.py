# pytest script for jumping the clouds, hacker rank problem.

import pytest
from jump_clouds import jump_clouds


@pytest.mark.parametrize(
    "c, result",
    [
        ([0, 0, 1, 0, 0, 1, 0], 4),
        ([0, 0, 0, 1, 0, 0], 3),
    ],
)
def test_jump_clouds(c, result):
    assert jump_clouds(c) == result
