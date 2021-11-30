# Find the lowest common ancestor. Given a Binary tree and two nodes

# Node for a binary tree
class Node:
    """Node of the binary tree."""

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return "({})".format(self.data)


class BinaryTree:
    """Binary tress class."""

    def __init__(self, py_list=[]):

        list_len = len(py_list)

        if list_len is None:
            print("Binary list empty")

        self.root = None

        for i in py_list:
            self.add_node(i)

    def add_node(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._add_helper(self.root, data)

    def _add_helper(self, sub_root, data):

        if data < sub_root.data:
            if sub_root.left is None:
                sub_root.left = Node(data)
            else:
                self._add_helper(sub_root.left, data)
        else:
            if sub_root.right is None:
                sub_root.right = Node(data)
            else:
                self._add_helper(sub_root.right, data)

    def __iter__(self):
        def inorder_traversal(sub_root):

            if sub_root.left:
                yield from inorder_traversal(sub_root.left)

            yield sub_root

            if sub_root.right:
                yield from inorder_traversal(sub_root.right)

        yield from inorder_traversal(self.root)

    def __str__(self) -> str:
        out = []
        for n in self:
            out.append(str(n.data))

        return ", ".join(out)


def find_ancestor(sub_root, v1, v2):
    """Find the lowest common ancestor in the given sub_root of the binary tree
        with two node values present in the binary tree as inputs (v1, v2)

    Args:
        sub_root (node): node of the binary tree
        v1 (int): first node value from the supplied binary tree
        v2 (int): secont node value from the supplied binary tree

    Returns:
        (node): returns Node representing the lowest common ancestor
    """

    if sub_root is None:
        return None
    if sub_root.data in [v1, v2]:
        return sub_root

    left_node = find_ancestor(sub_root.left, v1, v2)
    right_node = find_ancestor(sub_root.right, v1, v2)

    if left_node and right_node:
        return sub_root

    return left_node or right_node


if __name__ == "__main__":

    bt = BinaryTree([10, 6, 4, 5, 3, 7, 8, 9, 15, 14, 13, 16])
    print(bt)
    for _ in range(10):
        v1 = int(input("Enter v1 : "))
        v2 = int(input("Enter v2 : "))

        ancestor = find_ancestor(bt.root, v1, v2)
        print(
            "Lowest common ancestor value of v1:"
            + str(v1)
            + " and v2:"
            + str(v2)
            + " is : "
            + str(ancestor)
        )

        print("-" * 55)
