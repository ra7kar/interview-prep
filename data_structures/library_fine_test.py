# pytest scrip for library fine , hacker rank problem.

import pytest
from library_fine import library_fine


@pytest.mark.parametrize(
    "d1, m1, y1, d2, m2, y2, result",
    [
        (9, 6, 2015, 6, 6, 2015, 45),
        (9, 7, 2016, 6, 6, 2015, 10_000),
    ],
)
def test_library_fine(d1, m1, y1, d2, m2, y2, result):
    assert library_fine(d1, m1, y1, d2, m2, y2) == result
