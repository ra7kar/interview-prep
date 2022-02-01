# div_sum_pair: pytest script

import pytest
from div_sum_pair import divisible_sum_pairs


@pytest.mark.parametrize(
    "n, k, ar, result",
    [
        (6, 3, [1, 3, 2, 6, 1, 2], 5),
        (10, 3, [29, 97, 52, 86, 27, 89, 77, 19, 99, 96], 15),
    ],
)
def test_div_sum_pair(n, k, ar, result):
    assert divisible_sum_pairs(n, k, ar) == result
