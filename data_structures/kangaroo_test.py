# pytest for kangaroo.py, Hacker rank problem.

import pytest
from kangaroo import kangaroo


@pytest.mark.parametrize(
    "x1, v1, x2, v2, result",
    [(0, 3, 4, 2, "YES"), (0, 2, 5, 3, "NO")],
)
def test_kangaroo(x1, v1, x2, v2, result):

    assert kangaroo(x1, v1, x2, v2) == result
