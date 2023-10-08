# pytest script for electronic_shop program.

import pytest

from electronic_shop import get_money_spent


@pytest.mark.parametrize(
    "keyboards, drives, b, result",
    [([40, 50, 60], [5, 8, 12], 60, 58), ([3, 1], [5, 2, 8], 10, 9), ([4], [5], 5, -1)],
)
def test_get_money_spent(keyboards, drives, b, result):
    assert get_money_spent(keyboards, drives, b) == result
