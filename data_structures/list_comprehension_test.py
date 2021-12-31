# list comprehension pytest file.

# External
import pytest
from list_comprehension import list_comp


@pytest.mark.parametrize(
    "x,y,z,n, result",
    [
        (
            2,
            2,
            2,
            2,
            [
                [0, 0, 0],
                [0, 0, 1],
                [0, 1, 0],
                [0, 1, 2],
                [0, 2, 1],
                [0, 2, 2],
                [1, 0, 0],
                [1, 0, 2],
                [1, 1, 1],
                [1, 1, 2],
                [1, 2, 0],
                [1, 2, 1],
                [1, 2, 2],
                [2, 0, 1],
                [2, 0, 2],
                [2, 1, 0],
                [2, 1, 1],
                [2, 1, 2],
                [2, 2, 0],
                [2, 2, 1],
                [2, 2, 2],
            ],
        ),
        (1, 1, 1, 2, [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]),
    ],
)
def test_list_comprehension(x, y, z, n, result):
    ret_val = list_comp(x, y, z, n)

    assert ret_val == result
