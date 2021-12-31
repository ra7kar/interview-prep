# pytest for lowest common ancestor in a binary tree

# External
import pytest

# Internal
from lowest_common_ancestor import BinaryTree, find_ancestor


@pytest.mark.parametrize(
    "v1, v2, result",
    [
        (3, 5, 4),
        (9, 5, 6),
        (6, 13, 10),
        (8, 9, 8),
        (13, 16, 15),
    ],
)
def test_lowest_common_ancestor(v1, v2, result):
    bt = BinaryTree([10, 6, 4, 5, 3, 7, 8, 9, 15, 14, 13, 16])
    root = bt.root
    ancestor = find_ancestor(root, v1, v2)
    assert ancestor.data == result
