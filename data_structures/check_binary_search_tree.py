# check if the binary tree is a binary search tree.

from collections import deque


class Node:
    # create a Node class
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

    def __str__(self):
        lines, *_ = self._display_aux()
        return "\n".join(lines)

    def _display_aux(self):
        # https://stackoverflow.com/users/1143396/j-v?tab=profile
        # Thanks to JV for his code.
        # No child.
        if self.right is None and self.left is None:
            if self.height:
                line = "({}, {})".format(self.data, self.height)
            else:
                line = "({})".format(self.data)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            if self.height > 0:
                s = "({}, {})".format(self.data, self.height)
            else:
                s = "({})".format(self.data)
            u = len(s)
            first_line = (x + 1) * " " + (n - x - 1) * "-" + s
            second_line = x * " " + "/" + (n - x - 1 + u) * " "
            shifted_lines = [line + u * " " for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            if self.height:
                s = "({}, {})".format(self.data, self.height)
            else:
                s = "({})".format(self.data)
            u = len(s)
            first_line = s + x * "-" + (n - x) * " "
            second_line = (u + x) * " " + "\\" + (n - x - 1) * " "
            shifted_lines = [u * " " + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        if self.height:
            s = "({}, {})".format(self.data, self.height)
        else:
            s = "({})".format(self.data)
        u = len(s)
        first_line = (x + 1) * " " + (n - x - 1) * "-" + s + y * "-" + (m - y) * " "
        second_line = (
            x * " " + "/" + (n - x - 1 + u + y) * " " + "\\" + (m - y - 1) * " "
        )
        if p < q:
            left += [n * " "] * (q - p)
        elif q < p:
            right += [m * " "] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * " " + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


class BinaryTree:
    def __init__(self, py_list):
        self.root = None
        self.build_tree(py_list)

    def add_node(self, sub_root, n1=None, n2=None):
        sub_root.left = n1
        sub_root.right = n2

    def build_tree(self, py_list):
        py_list_len = len(py_list)
        q = deque()
        # create the root
        if py_list_len == 0:
            return self

        self.root = Node(py_list[0])
        sub_root = self.root
        for i in range(1, py_list_len, 2):
            n1 = Node(py_list[i])
            q.append(n1)
            try:
                n2 = Node(py_list[i + 1])
                q.append(n2)
            except IndexError:
                n2 = None

            self.add_node(sub_root, n1, n2)

            sub_root = q.popleft()

        return self

    # check if binary tree is a binary search tree
    def is_binary_search_tree(self):
        sub_root = self.root
        bt_list = []
        if self.root is None:
            return (True, self, None, None)

        def get_val(sub_root, bt_list):
            """In-order traversal

            Args:
                sub_root (Node object): Node of the binary tree
                bt_list (list): list to capture the binary tree values
            """

            if sub_root.left:
                get_val(sub_root.left, bt_list)

            val = sub_root.data
            bt_list.append(val)

            if sub_root.right:
                get_val(sub_root.right, bt_list)

        get_val(sub_root, bt_list)

        # check if bt_list is in assending order.
        bt_len = len(bt_list)
        for i in range(bt_len):
            v1 = bt_list[i]
            if i < bt_len - 1:
                v2 = bt_list[i + 1]
            else:
                return (True, bt_list, None, None)

            if v1 is None or v2 is None:
                continue

            if v1 > v2:
                return (False, bt_list, v1, v2)

        return (True, bt_list, None, None)


# -------Main------------------
if __name__ == "__main__":
    py_list = [10, 3, 8, 2, 6, 7, 1]  # - False
    py_list = [34, 3, 36, 2, 8, 35, 37, 1]  # - True
    py_list = [10, 3, 15, 5, 12, 2, 16, 1]  # - False
    py_list = [14, 3, 15, 5, 12, 2, 16, 1]  # - False
    py_list = [34, 3, 35, 5, 12, 2, 16, 1]  # - False
    py_list = [34, 3, 37, 2]  # - True
    py_list = [1, 2, 4, 3, 5, 6, 7]  # - False
    py_list = [3, 2, 6, 1, 4, 5, 7]  # - False
    py_list = [1, 2, 3, 4, 5, 6, 7]  # - False
    py_list = [1, None, 2, None, None, None, 3]
    py_list = [10, 3, 89, 2, 5, 56, 54]

    bt = BinaryTree(py_list)
    print("List is :", end="")
    print(py_list)
    print("Binary tree is :")
    print(bt.root)
    ret_val, bt_list, v1, v2 = bt.is_binary_search_tree()
    if ret_val:
        print("Tree is a Binary Search Tree")
    else:
        print("Not a Binary search tree")
        print("Issue is at: " + "v1:" + str(v1) + "   v2:" + str(v2))
    print(bt_list)
