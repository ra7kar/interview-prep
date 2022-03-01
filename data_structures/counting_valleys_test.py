# pytest script for counting_vallyes program

import pytest
from counting_valleys import counting_valleys


@pytest.mark.parametrize(
    "steps, path, result",
    [
        (8, "UDDDUDUU", 1),
        (12, "DDUUDDUDUUUD", 2),
    ],
)
def test_counting_valleys(steps, path, result):
    assert counting_valleys(steps, path) == result
