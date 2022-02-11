# Binary/Linear search pytest program.

import pytest
from search import Search_Type
from search import search


@pytest.mark.parametrize(
    "search_type, search_number, py_list, result",
    [
        (Search_Type.BINARY, 7, [1, 2, 3, 4, 5, 6], False),
        (Search_Type.BINARY, 6, [1, 23, 4, 5, 6], True),
        (Search_Type.LINEAR, 7, [1, 2, 3, 4, 5, 6], False),
        (Search_Type.LINEAR, 6, [1, 2, 3, 4, 5, 6], True),
    ],
)
def test_search(search_type, search_number, py_list, result):

    assert search(search_type, search_number, py_list) == result
