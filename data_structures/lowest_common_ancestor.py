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
    """Binary tress."""

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


def find_ancestor(root, n1, n2):
    """Find the lowest common ancestor in the given root of the binary tree
        with two node values present in the binary tree as inputs (n1, n2)

    Args:
        root (object): Binary tree root object
        n1 (int): first node value from the supplied binary tree
        n2 (int): secont node value from the supplied binary tree

    Returns:
        (int): intiger valu [description]
    """

    if root is None:
        return None
    if root.data == n1 or root.data == n2:
        return root.data

    left_node = find_ancestor(root.left, n1, n2)
    right_node = find_ancestor(root.right, n1, n2)

    if left_node is not None and right_node is not None:
        return root.data
    if left_node is not None:
        return left_node
    else:
        return right_node


if __name__ == "__main__":

    bt = BinaryTree([10, 6, 4, 5, 3, 7, 8, 9, 15, 14, 13, 16])
    print(bt)
    for _ in range(10):
        n1 = int(input("Enter N1 : "))
        n2 = int(input("enter N2 : "))
        ancestor = find_ancestor(bt.root, n1, n2)
        print(
            "Lowest common ancestor value of n1:"
            + str(n1)
            + " and n2:"
            + str(n2)
            + " is : "
            + str(ancestor)
        )

        print("-" * 55)
