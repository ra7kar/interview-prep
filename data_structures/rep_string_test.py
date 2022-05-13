# pytest for repeated string, hacker rank problem.

import pytest
from rep_string import rep_string


@pytest.mark.parametrize(
    "s, n, result",
    [
        ("aba", 10, 7),
        ("a", 1000000000000, 1000000000000),
    ],
)
def test_rep_string(s, n, result):
    assert rep_string(s, n) == result
