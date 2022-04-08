# pytest script for utopian tree, hacker rank problem

import pytest
from utopian_tree import utopian_tree


@pytest.mark.parametrize(
    "n, result",
    [
        (5, 14),
        (21, 4094),
        (3, 6),
    ],
)
def test_utopian_tree(n, result):
    assert utopian_tree(n) == result
