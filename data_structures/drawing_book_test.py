# pytest script for drawing board program

import pytest

from drawing_book import drawing_book


@pytest.mark.parametrize(
    "n, p, result",
    [
        (11, 7, 2),
        (7, 4, 1),
    ],
)
def test_drawing_book(n, b, result):
    assert drawing_book(n, b) == result
