# implement a Trie.


class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def add_word(self, word):

        cur_node = self.root

        for char in word:
            if char not in cur_node.children:
                cur_node.children[char] = TrieNode()
            cur_node = cur_node.children[char]

        cur_node.end_of_word = True

    def search(self, word):
        cur_node = self.root
        ret_val = False

        if word:
            for char in word:
                if char in cur_node.children:
                    cur_node = cur_node.children[char]

                    if cur_node.end_of_word:
                        ret_val = True
                    else:
                        ret_val = False
                else:
                    return False

        return ret_val

    def start_with(self, word):

        cur_node = self.root
        ret_val = True

        for letter in word:
            if letter in cur_node.children:
                cur_node = cur_node.children[letter]
            else:
                return False

        return ret_val

    def __repr__(self):
        def recur(node, indent):
            return "".join(
                indent
                + key
                + ("$" if child.end_of_word else "")
                + recur(child, indent + "  ")
                for key, child in node.children.items()
            )

        return recur(self.root, "\n")


if __name__ == "__main__":

    trie = Trie()
    trie.add_word("apple")
    trie.add_word("at")
    trie.add_word("att")
    trie.add_word("btt")
    print("-" * 25)
    search_w = "battt"
    print("search word: {}  --> {}".format(search_w, trie.search(search_w)))
    print("-" * 25)
    start_w = "at"
    print("Word Starts with: {} --> {}".format(start_w, trie.start_with(start_w)))
    print("-" * 25)

    print(trie)
