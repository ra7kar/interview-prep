# pytest for beautiful triplets
# hacker rank problem.

import pytest
from beautiful_triplets import beautiful_triplets


@pytest.mark.parametrize(
    "d, arr, result",
    [
        (3, [1, 2, 4, 4, 5, 7, 8, 10], 4),
        (3, [1, 2, 4, 5, 7, 8, 10], 3),
    ],
)
def test_beautiful_triplets(d, arr, result):
    assert beautiful_triplets(d, arr) == result
