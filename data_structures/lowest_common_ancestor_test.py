# pytest for lowest common ancestor in a binary tree

# External
import pytest

# Internal
from lowest_common_ancestor import BinaryTree, find_ancestor

bt = BinaryTree([10, 6, 4, 5, 3, 7, 8, 9, 15, 14, 13, 16])
root = bt.root
n1_1 = 3  # test 1
n2_1 = 5
r_1 = 4
n1_2 = 9  # test 2
n2_2 = 5
r_2 = 6
n1_3 = 6  # test 3
n2_3 = 13
r_3 = 10
n1_4 = 8  # test 4
n2_4 = 9
r_4 = 8
n1_5 = 13  # test 5
n2_5 = 16
r_5 = 15


@pytest.mark.parametrize(
    "root, n1, n2, result",
    [
        (root, n1_1, n2_1, r_1),
        (root, n1_2, n2_2, r_2),
        (root, n1_3, n2_3, r_3),
        (root, n1_4, n2_4, r_4),
        (root, n1_5, n2_5, r_5),
    ],
)
def test_lowest_common_ancestor(root, n1, n2, result):

    ancestor = find_ancestor(root, n1, n2)
    assert ancestor == result
