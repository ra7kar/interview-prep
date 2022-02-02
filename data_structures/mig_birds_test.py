# mig_birds: pytest script

import pytest
from mig_birds import migratory_birds


@pytest.mark.parametrize(
    "py_list, result",
    [
        ([1, 1, 2, 20, 1, 3, 3, 3, 7], 1),
        ([1, 2, 3, 6, 6, 7, 20, 4, 5, 4, 3, 2, 1, 3, 4], 3),
    ],
)
def test_migratory_birds(py_list, result):
    assert migratory_birds(py_list) == result
