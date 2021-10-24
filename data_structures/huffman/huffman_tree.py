
from os import curdir
import struct
from collections import defaultdict
from functools import lru_cache
from queue import Empty, PriorityQueue

class Node:
    def __init__(self, count, char=None, parent=None, left=None, right=None) -> None:
        self.count = count
        self.char = char
        self.parent = parent

        self.left = left
        if left:
            left.parent = self

        self.right = right
        if right:
            right.parent = self

        height_left = left.height if left else 0
        height_right = right.height if right else 0
        self.height = max(height_left, height_right) + 1
    
    def __lt__(self, other):
        return self.count < other.count

    def __str__(self) -> str:
        lines, *_ = self._display_aux()
        return "\n".join(lines)
    
    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = "({}, {})".format(self.count, self.char)
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = "({}, {})".format(self.count, self.char)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = "({}, {})".format(self.count, self.char)
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = "({}, {})".format(self.count, self.char)
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

        
class HuffmanTree:
    def __init__(self, input_file, output_file, action) -> None:
        self.input_file = input_file
        self.output_file = output_file
        self.action = action

        # Tree attributes
        self.root = None
        self.char_to_node = {}

        self._generate_tree()
    
    def _generate_tree(self):
        if self.action == "compress":
            self._generate_tree_from_raw()
        else:
            self._generate_tree_from_compressed()

    def _generate_tree_from_compressed(self):
        pass
    
    def _generate_tree_from_raw(self):
        # Count chars in file
        chars_count = defaultdict(int)
        with open(self.input_file, "r") as file:
            for line in file:
                for char in line:
                    chars_count[char] += 1

        # Init pq with counts
        pq = PriorityQueue()
        for char, count in chars_count.items():
            # Create node and add it to dictionary
            node = Node(count, char=char)
            self.char_to_node[char] = node

            # Add all leaf nodes to pq
            pq.put(node)
        
        # Generate tree
        while not pq.empty():
            first = pq.get(block=False)

            try:
                second = pq.get(block=False)
            except Empty:
                self.root = first
                return
            
            parent = Node(first.count + second.count, left=first, right=second)
            pq.put(parent)
            
        assert False, "Tree generation is broken. Root was not discovered."

    def compress(self):
        output = ""

        # Open input and output files
        with open(self.output_file, "w", buffering=1000) as out_f, \
            open(self.input_file, "r") as in_f:
            # Read line from input file
            for line in in_f:
                # Read char from input file line
                for char in line:
                    # Compress character and add to output stream
                    output += self._compress_char(char)

                    # If output is greater than 8, it can be written as a char
                    if len(output) >= 8:
                        # Create and write packed version of bit stream
                        out_f.write(chr(int(output[0:8], base=2)))

                        # Clear output of the written bits
                        output = output[8:]
                    
            if len(output) > 0:
                output.ljust(8, "0")
                out_f.write(chr(int(output[0:8], base=2)))
        
    @lru_cache(maxsize=None)
    def _compress_char(self, char):
        node = self.char_to_node[char]
        
        if node is self.root:
            return "0"
        
        compressed = ""
        while node.parent != None:
            temp = node.parent
            if temp.left is node:
                compressed += "0"
            else:
                compressed += "1"
            node = node.parent

        return compressed

        


    def decompress(self):
        pass

    def __str__(self) -> str:
        return str(self.root)
   
    def __iter__(self):
        def _inorder_traversal(subroot):
            if subroot.left is not None:
                yield from _inorder_traversal(subroot.left)

            yield subroot

            if subroot.right is not None:
                yield from _inorder_traversal(subroot.right)

        yield from _inorder_traversal(self.root)