# pytest for non divisible subset , hacker rank problem.

import pytest
from non_div_subset import non_div_subset


@pytest.mark.parametrize(
    "k, s, result",
    [
        (
            7,
            [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436],
            11,
        ),
        (3, [1, 7, 2, 4], 3),
        (4, [1, 3, 4, 5, 6], 4),
    ],
)
def test_non_div_subset(k, s, result):
    assert non_div_subset(k, s) == result


# [
#     (7,
#     [278, 576, 496, 727, 410, 124, 338, 149, 209, 702, 282, 718, 771, 575, 436],
#     11),
#     (3,
#     [1, 7, 2, 4],
#     3)
#     (4,
#     [1, 3, 4, 5, 6],
#     4 ),
# ],
# )
