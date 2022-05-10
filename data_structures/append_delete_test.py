# pytest script for append delete - hacker rank problem.

import pytest
from append_delete import append_delete


@pytest.mark.parametrize(
    "s, f, k, result",
    [
        ("abcd, defg, 7", "No"),
        ("hackerhappy, hackerrank, 9", "Yes"),
        ("aba, aba, 7", "Yes"),
    ],
)
def test_append_delete(s, f, k, result):
    assert append_delete(s, f, k) == result
