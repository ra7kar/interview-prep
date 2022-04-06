# Climbing_leader_board, hacker rank problem.

import pytest
from climbing_leader_board import climbing_leaderboard


@pytest.mark.parametrize(
    "ranked, player, result",
    [
        ([100, 70, 90, 90, 80], [70, 80, 105], [4, 3, 1]),
        ([130, 90, 90, 80], [70, 80, 105], [4, 3, 2]),
    ],
)
def test_climbing_leader_board(ranked, player, result):
    assert climbing_leaderboard(ranked, player) == result
