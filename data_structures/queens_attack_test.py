# pytest script for queens attack , hacker rank problem.

import pytest
from queens_attack import queens_attack


@pytest.mark.parametrize(
    "n, k, r_q, c_q, obstacles, result",
    [
        (5, 3, 4, 3, [(5, 5), (4, 2), (2, 3)], 10),
        (5, 3, 4, 3, [(5, 5), (4, 2), (2, 3), (3, 2)], 8),
    ],
)
def test_queens_attack(n, k, r_q, c_q, obstacles, result):
    assert queens_attack(n, k, r_q, c_q, obstacles) == result
