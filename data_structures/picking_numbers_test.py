# pytest script for picking numbers, Hacker rank problem.

import pytest
from picking_numbers import picking_numbers


@pytest.mark.parametrize(
    "arr, result",
    [
        ([1, 2, 4, 4, 4, 5], 4),
        ([1, 2, 4, 4, 4, 6], 3),
    ],
)
def test_picking_numbers(arr, result):
    assert picking_numbers(arr) == result
