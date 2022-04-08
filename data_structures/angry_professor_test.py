# pytest script for angry professor

import pytest
from angry_professor import angry_professor


@pytest.mark.parametrize(
    "k, a, result",
    [
        (4, [-2, -1, 4, 2], "YES"),
        (2, [-2, -1, 4, 2], "NO"),
    ],
)
def test_angry_professor(k, a, result):
    assert angry_professor(k, a) == result
