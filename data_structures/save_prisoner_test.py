# pytest script for save the prisoner, hacker rank problem

import pytest
from save_prisoner import save_prisoner


@pytest.mark.parametrize(
    "n, m, s, result",
    [
        (3, 7, 3, 3),
        (5, 3, 3, 5),
    ],
)
def test_save_prisoner(n, m, s, result):
    assert save_prisoner(n, m, s) == result
