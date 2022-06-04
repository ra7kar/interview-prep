# Tree class.

ret_list = []


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.children = []
        self.parent = None
        self.count = 0

    def __str__(self) -> str:
        return self.data

    def print_tree(self):
        space = "" + " " * self.get_level() * 3
        prefix = space + "|--" if self.parent else ""
        print(prefix + str(self.data))
        for child in self.children:
            child.print_tree()

    def tree_list(self, ret_list):
        ret_list.append(self.data)
        for child in self.children:
            child.tree_list(ret_list)

        return ret_list

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        self.count += 1

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def get_root(self):
        p = self.parent
        p = p.parent

        return p  # p is the root node now as parent is None for Root.


def build_tree(dic):
    if dic:
        list = dic.keys()
        # node_list = []
        for item in list:
            globals()["%s" % item] = TreeNode(item)
            # node_list.append(globals()['%s' %item])

        for key, val in dic.items():
            for i in val:
                # if i not in dic.keys():
                globals()["%s" % i] = TreeNode(i)

                if i != key:

                    globals()["%s" % key].add_child(globals()["%s" % i])

        root = globals()["%s" % i].get_root()

    return root


if __name__ == "__main__":

    tree = {
        "Electronics": ["Laptops", "TVs", "Cellphones"],
        "Laptops": ["Lenovo", "HP"],
        "TVs": ["Samsung", "LG"],
        "Cellphones": ["Apple"],
    }

    root = build_tree(tree)
    root.print_tree()
    root.tree_list(ret_list)
    print(ret_list)

    print()
