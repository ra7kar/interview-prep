# pytest for jumping clouds, hacker rank problem

import pytest
from jumping_clouds import jumping_clouds


@pytest.mark.parametrize(
    "c, k, result",
    [
        ([0, 0, 1, 0, 0, 1, 1, 0], 2, 92),
        ([1, 1, 1, 0, 1, 1, 0, 0, 0, 0], 3, 80),
    ],
)
def test_jumping_clouds(c, k, result):
    assert jumping_clouds(c, k) == result
