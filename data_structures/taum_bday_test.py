# pytest script for taum and bday, hacker rank problem.

import pytest
from taum_bday import taum_bday


@pytest.mark.parametrize(
    "b,bc,w,wc,z,result",
    [
        (3, 1, 3, 9, 2, 12),
        (7, 4, 7, 2, 1, 35),
    ],
)
def test_taum_bday(b, bc, w, wc, z, result):
    assert taum_bday(b, bc, w, wc, z) == result
