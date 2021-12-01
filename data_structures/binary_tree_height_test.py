# binary tree height test file

# Internal
from binary_tree_height import BinaryTree, bt_height

# External
import pytest


@pytest.mark.parametrize(
    "pylist, result",
    [
        ([10, 6, 4, 7, 14, 12, 13, 11, 3, 5, 2], 5),
        ([22, 23, 16, 17, 4, 18, 5, 12], 5),
        ([24, 19, 10, 4, 12, 11, 9, 20, 8], 6),
        ([8, 18, 22, 2, 10, 15, 1, 7], 4),
        ([4, 10, 20, 14, 15, 24, 19, 23], 6),
    ],
)
def test_binary_tree_height(pylist, result):
    bt = BinaryTree(pylist)
    height = bt_height(bt.root)
    assert height == result
