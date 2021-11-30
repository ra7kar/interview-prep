# Find the binary tree height

# Binary Tree --------
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

    def __str__(self):
        lines, *_ = self._display_aux()
        return "\n".join(lines)

    def _display_aux(self):
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
    def __init__(self, pylist=[]) -> None:
        self.root = None

        for i in pylist:
            self.add(i)

    def add(self, data):

        if self.root is None:
            self.root = Node(data)
        else:
            self._helper_add(self.root, data)

    def _helper_add(self, sub_root, data):
        if data < sub_root.data:
            if sub_root.left is None:
                sub_root.left = Node(data)
            else:
                self._helper_add(sub_root.left, data)
        elif data > sub_root.data:
            if sub_root.right is None:
                sub_root.right = Node(data)
            else:
                self._helper_add(sub_root.right, data)

    def __iter__(self):
        def in_order_traversal(sub_root):
            if sub_root.left is not None:
                yield from in_order_traversal(sub_root.left)

            yield sub_root

            if sub_root.right is not None:
                yield from in_order_traversal(sub_root.right)

        yield from in_order_traversal(self.root)

    def __str__(self) -> str:
        return ", ".join(str(i.data) for i in self)


def bt_height(sub_root):
    if sub_root is None:
        return 0

    left_side = bt_height(sub_root.left)
    right_side = bt_height(sub_root.right)

    if left_side > right_side:
        height = 1 + left_side
    else:
        height = 1 + right_side

    return height


# --------------------------- Main -----------------------
if __name__ == "__main__":

    pylist = [10, 6, 4, 7, 14, 12, 13, 11, 3, 5, 2]

    bt = BinaryTree(pylist)
    print()
    print(bt.root)
    print("-" * 55)
    print("Binary Tree is : ", end="")
    print(pylist)
    print("Binary Tree height is : " + str(bt_height(bt.root)))
