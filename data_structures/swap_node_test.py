# test cases for swap_nodes.

import pytest

from swap_nodes import swap_nodes


@pytest.mark.parametrize(
    "indexes, queries, result",
    [
        (
            [[2, 3], [4, 5], [6, 7], [8, 9]],
            [2, 2],
            [[7, 3, 6, 1, 5, 2, 8, 4, 9], [8, 4, 9, 2, 5, 1, 6, 3, 7]],
        ),
        (
            [[2, 3], [4, 5], [6, 7], [8, 9]],
            [2, 2, 3],
            [
                [7, 3, 6, 1, 5, 2, 8, 4, 9],
                [8, 4, 9, 2, 5, 1, 6, 3, 7],
                [6, 3, 7, 1, 9, 4, 8, 2, 5],
            ],
        ),
    ],
)
def test_swap_nodes(indexes, queries, result):
    ret_val = swap_nodes(indexes, queries)
    assert ret_val == result
