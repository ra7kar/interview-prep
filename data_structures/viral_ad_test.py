# pytest script for viral advertising , hacker rank problem

import pytest
from viral_ad import viral_adv


@pytest.mark.parametrize(
    "n, result",
    [
        (5, 24),
        (4, 15),
        (3, 9),
    ],
)
def test_viral_ad(n, result):
    assert viral_adv(n) == result
