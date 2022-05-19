# pytest for ACM-ICPC World Finals, Hacker rank problems.

import pytest
from acm_meet import acm_meet


@pytest.mark.parametrize(
    "topics, result",
    [
        (["10101", "11110", "00010"], [5, 1]),
        (["10101", "11100", "11010", "00101"], [5, 2]),
        (["11101", "10101", "11001", "10111", "10000", "01110"], [5, 6]),
    ],
)
def test_acm_meet(topics, result):
    assert acm_meet(topics) == result
