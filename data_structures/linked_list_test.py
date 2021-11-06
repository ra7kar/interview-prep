# Std
import random

# External
import pytest

# Internal
from linked_list import LinkedList, Node


@pytest.mark.parametrize("input", [[], [0], [1, 0], [0, 1, 0], [9, 9, 9]])
def test_linked_list(input):
    ll = LinkedList(input)

    assert len(ll) == len(input), "Length of linked list and input do not match."

    for idx, pair in enumerate(zip(input, ll)):
        (val, node) = pair
        assert (
            val == node.data
        ), "Linked list and input differ at idx " "{}: val={}, node.data={}".format(
            idx, val, node.data
        )


def test_node():
    input = random.randint(0, 10000)
    node = Node(input)
    assert (
        input == node.data
    ), "Node value and input differ " "val={}, node.data={}".format(input, node.data)
