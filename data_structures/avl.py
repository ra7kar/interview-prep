# AVL Tree v02

import random

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.height = 1

    def __str__(self):
        lines, *_ = self._display_aux()
        return "\n".join(lines)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = "({}, {})".format(self.data, self.height)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = "({}, {})".format(self.data, self.height)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = "({}, {})".format(self.data, self.height)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = "({}, {})".format(self.data, self.height)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
            '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
            (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

class AVLTree:
    def __init__(self, pylist=[]):
        self.root = None
        for i in pylist:
            self.insert(i)

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.root = self._insert(self.root, data)
        print("="*30 + str(data) + "="*30)
        print(self)

    def _insert(self, subroot, data):

        if data == subroot.data:
            return subroot

        if data < subroot.data:
            if subroot.left is None:
                subroot.left = Node(data)
            else:
                subroot.left = self._insert(subroot.left, data)
        elif data > subroot.data:
            if subroot.right is None:
                subroot.right = Node(data)
            else:
                subroot.right = self._insert(subroot.right, data)

        # Update heights
        height_left = subroot.left.height if subroot.left else 0
        height_right = subroot.right.height if subroot.right else 0
        subroot.height = max(height_left, height_right) + 1

        # assing the new root to return.
        new_root = subroot
     
        # check if imbalance exist
        if abs(height_left-height_right) > 1:
            new_root = self._fix_imbalance(subroot, height_left, height_right)

        return new_root

    def _fix_imbalance(self, subroot, height_left, height_right):
        if height_left > height_right:  # left heavy
            
            # get left , left and right heights
            left_left_height = subroot.left.left.height if subroot.left.left else 0
            left_right_height = subroot.left.right.height if subroot.left.right else 0

            if left_left_height > left_right_height : # left left heavy
                #right rotate
                new_root = AVLTree._right_rotate(subroot)
            else:
                # left right rotate left right heavy
                new_root = AVLTree._left_right_rotate(subroot)

        else:

            right_left_height = subroot.right.left.height if subroot.right.left else 0
            right_right_height = subroot.right.right.height if subroot.right.right else 0

            if right_right_height > right_left_height: # right right heavy
                #left rotate
                new_root = AVLTree._left_rotate(subroot)
            else:
                # right left rotate    right left heavy
                new_root = AVLTree._right_left_rotate(subroot)

        AVLTree._fix_height(new_root)

        return new_root



    @staticmethod
    def _right_rotate(subroot):
        new_root = subroot.left
        subroot.left = new_root.right
        new_root.right = subroot



        return new_root
    
    @staticmethod
    def _left_right_rotate(subroot):
        new_root = subroot.left.right
        subroot.left.right = new_root.left
        subroot.left.height = 1
        new_root.left = subroot.left
        subroot.left = new_root.right
        new_root.right = subroot

        return new_root

    def _left_rotate(subroot):
        
        new_root = subroot.right
        subroot.right = new_root.left
        new_root.left = subroot

        return new_root

    @staticmethod
    def _right_left_rotate(subroot):

        new_root = subroot.right.left
        subroot.right.left = new_root.right
        subroot.right.height = 1
        new_root.right = subroot.right
        subroot.right = new_root.left
        new_root.left = subroot

        return new_root

    @staticmethod
    def _fix_height(subroot):
        if subroot is None:
            return 0

        left_height = AVLTree._fix_height(subroot.left)
        right_height = AVLTree._fix_height(subroot.right)
        
        subroot.height = max(left_height, right_height) + 1
        
        return subroot.height
    
    def __str__(self):
        return str(self.root)

    def __iter__(self):
        def _inorder_traversal(subroot):
            if subroot.left is not None:
                yield from _inorder_traversal(subroot.left)

            yield subroot

            if subroot.right is not None:
                yield from _inorder_traversal(subroot.right)

        yield from _inorder_traversal(self.root)


ll = [] #[6,3,7,1,4,5]
t = AVLTree(ll)

if len(ll) == 0:
    insert_list = [random.randint(0, 10) for _ in range(10)]

    for i in insert_list:
        t.insert(i)

    print("Insert list: {}".format(insert_list))

#print(t)