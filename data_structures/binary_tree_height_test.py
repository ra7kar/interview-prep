# binary tree height test file

# Internal
from binary_tree_height import BinaryTree, bt_height

# External
import pytest


@pytest.mark.parametrize("pylist, result", [10, 6, 4, 7, 14, 12, 13, 11, 3, 5, 2], 5)
def test_binary_tree_height(pylist, result):
    bt = BinaryTree(pylist)
    height = bt_height(bt.root)
    assert height == result
