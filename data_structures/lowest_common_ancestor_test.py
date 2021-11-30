# pytest for lowest common ancestor in a binary tree

# External
import pytest

# Internal
from lowest_common_ancestor import BinaryTree, find_ancestor

bt = BinaryTree([10, 6, 4, 5, 3, 7, 8, 9, 15, 14, 13, 16])


@pytest.mark.parametrize(
    "bt, v1, v2, result",
    [
        (bt, 3, 5, 4),
        (bt, 9, 5, 6),
        (bt, 6, 13, 10),
        (bt, 8, 9, 8),
        (bt, 13, 16, 15),
    ],
)
def test_lowest_common_ancestor(bt, v1, v2, result):
    sub_root = bt.sub_root
    ancestor = find_ancestor(sub_root, v1, v2)
    assert ancestor == result
