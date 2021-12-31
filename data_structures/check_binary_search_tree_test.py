# test file for check_binary_search_tree.

import pytest
from check_binary_search_tree import BinaryTree


@pytest.mark.parametrize(
    "py_list, result",
    [
        ([10, 3, 8, 2, 6, 7, 1], False),
        ([34, 3, 36, 2, 8, 35, 37, 1], True),
        ([10, 3, 15, 5, 12, 2, 16, 1], False),
        ([14, 3, 15, 5, 12, 2, 16, 1], False),
        ([34, 3, 35, 5, 12, 2, 16, 1], False),
        ([34, 3, 37, 2], True),
        ([1, 2, 4, 3, 5, 6, 7], False),
        ([3, 2, 6, 1, 4, 5, 7], False),
        ([1, 2, 3, 4, 5, 6, 7], False),
        ([1, None, 2, None, None, None, 3], True),
        ([10, 3, 89, 2, 5, 56, 54], False),
    ],
)
def test_check_binary_search_tree(py_list, result):
    bt = BinaryTree(py_list)
    ret_val, bt_list, v1, v2 = bt.is_binary_search_tree()
    assert ret_val == result
