# pytest script for circular array rotation, hacker rank problem.

import pytest
from cir_array_rotation import circular_array_rotation


@pytest.mark.parametrize(
    "a, k, queries, result",
    [
        ([3, 4, 5, 6, 7], 2, [1, 2], [7, 3]),
        ([3, 4, 5, 6, 7], 3, [1, 2], [6, 7]),
    ],
)
def test_cir_array_rotation(a, k, queries, result):
    assert circular_array_rotation(a, k, queries) == result
