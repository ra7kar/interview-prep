# pytest script for cat and mouse program.

import pytest
from cat_and_mouse import cat_and_mouse


@pytest.mark.parametrize(
    "x, y, z, result",
    [
        (2, 5, 4, "Cat B"),
        (1, 3, 2, "Mouse C"),
        (5, 2, 4, "Cat A"),
    ],
)
def test_cat_and_mouse(x, y, z, result):
    assert cat_and_mouse(x, y, z) == result
