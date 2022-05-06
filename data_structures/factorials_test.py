# pytest for factorials, hacker rank problem.

import pytest
from factorials import factorial


@pytest.mark.parametrize(
    "n, result",
    [(25, 15511210043330985984000000), (20, 2432902008176640000), (4, 24)],
)
def test_factorial(n, result):
    assert factorial(n) == result
