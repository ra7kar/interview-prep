# pytest for Orgnize containers, hacker rank problem.

import pytest
from org_containers import org_containers


@pytest.mark.parametrize(
    "container, result",
    [
        ([[1, 4], [2, 3]], "Impossible"),
        ([[1, 3, 1], [2, 1, 2], [3, 3, 3]], "Impossible"),
        ([[0, 2, 1], [1, 1, 1], [2, 0, 0]], "Possible"),
    ],
)
def test_org_containers(container, result):
    assert org_containers(container) == result
