# pytest script for Bigger is greater, hacker rank problem.

import pytest

from bigger_greater import bigger_is_greater


@pytest.mark.parametrize(
    "w, result",
    [
        ("bb", "no answer"),
        ("dkhc", "hcdk"),
    ],
)
def test_bigger_greater(w, result):
    assert bigger_is_greater(w) == result
