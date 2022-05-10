# pytest script for append delete - hacker rank problem.

import pytest
from append_delete import append_delete


@pytest.mark.parametrize(
    "s, f, k, result",
    [
        ("ashley", "ash", 2, "No"),
        ("hackerhappy", "hackerrank", 9, "Yes"),
        ("aba", "aba", 7, "Yes"),
    ],
)
def test_append_delete(s, f, k, result):
    assert append_delete(s, f, k) == result
