# Huffman coding.


from collections import Counter
import heapq


class HuffmanCoding:
    def __init__(self):
        self.heap = []
        self.codes = {}

    class HeapNode:
        def __init__(self, char, freq) -> None:
            self.char = char
            self.freq = freq
            self.left = None
            self.right = None

        def __lt__(self, other):
            return self.freq < other.freq

        def __eq__(self, other):
            if other is None:
                return False
            if not (isinstance(other, self.HeapNode)):
                return

            return self.freq == other.freq

    def create_freq(self, text):
        return Counter(text)

    def create_min_heap(self, frequency):
        for key in frequency:
            node = self.HeapNode(key, frequency[key])
            heapq.heappush(self.heap, node)

    def create_huffman_tree(self):

        while len(self.heap) > 1:
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)
            merged = self.HeapNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2
            heapq.heappush(self.heap, merged)

    def create_codes_helper(self, node, code):
        if node is None:
            return
        if node.char is not None:
            if node.char in self.codes:
                self.codes[node.char] += code
            else:
                self.codes[node.char] = code
        else:
            self.create_codes_helper(node.left, code + "0")
            self.create_codes_helper(node.right, code + "1")

    def create_codes(self):
        root = self.heap[0]
        code = ""
        self.create_codes_helper(root, code)

    def encoded_text(self, text):
        ret_text = ""
        for char in text:
            ret_text += self.codes[char] + " "

        ret_text = ret_text.rstrip(" ")
        return ret_text

    def compress(self, text):

        # create frequency count of text
        frequency = self.create_freq(text)

        # create heap from the counter
        self.create_min_heap(frequency)

        # merge nodes and create huffman tree
        self.create_huffman_tree()

        # create codes
        self.create_codes()

        # print codes
        return self.encoded_text(text)


if __name__ == "__main__":

    text = "444225"
    text = "adbcacc"
    text = "abac"
    text = "adbcacc"

    print(text)
    hc = HuffmanCoding()

    print(hc.compress(text))
