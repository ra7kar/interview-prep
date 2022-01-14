"""Swap nodes of binary tree at the Kth level, root being at level 1
    Problem from Hacker Rank.
    https://www.hackerrank.com/challenges/swap-nodes-algo/problem?isFullScreen=true

Citations:
    To display the binary tree I have used the reference from:
    https://stackoverflow.com/users/1143396/j-v

"""

from collections import deque


class Node:
    def __init__(self, data):
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


def swap_nodes(indexes, queries):
    def build_tree(root, indexes):
        sub_root = root
        q = deque([sub_root])

        for left, right in indexes:
            sub_root = q.popleft()
            if left > 1:
                sub_root.left = Node(left)
                q.append(sub_root.left)
            if right > 1:
                sub_root.right = Node(right)
                q.append(sub_root.right)

        return root

    def perform_swap(root, k, level, l_list):
        if root:
            if k % level == 0:
                # perform the node swap.
                root.left, root.right = root.right, root.left

            # in_order traversal.
            perform_swap(root.left, k, level + 1, l_list)
            l_list.append(root.data)
            perform_swap(root.right, k, level + 1, l_list)

        return l_list

    # create the root
    root = Node(1)

    # build the binary tree
    root = build_tree(root, indexes)

    # perform swap based on queries
    ret_val = []
    for k in queries:
        l_list = []
        perform_swap(root, k, 1, l_list)
        ret_val.append(l_list)

    return ret_val


# main -----------------------------------------


def main():

    indexes = [[2, 3], [4, 5], [6, 7], [8, 9]]
    queries = [2, 2, 3]

    ret_val = swap_nodes(indexes, queries)

    print(ret_val)


if __name__ == "__main__":
    main()
