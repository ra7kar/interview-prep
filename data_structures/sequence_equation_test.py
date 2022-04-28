# pytest script for sequence equation, hacker rank problem

import pytest
from sequence_equation import permutation_equation


@pytest.mark.parametrize(
    "p, result",
    [
        ([5, 2, 1, 3, 4], [4, 2, 5, 1, 3]),
        ([2, 3, 1], [2, 3, 1]),
        ([4, 3, 5, 1, 2], [1, 3, 5, 4, 2]),
    ],
)
def test_sequence_equation(p, result):
    assert permutation_equation(p) == result
