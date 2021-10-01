# LinkedList

class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next

    def __str__(self) -> str:
        return "({})".format(self.data)

    def print(self) -> str:
        ## Recursive
        if self.next:
            connected = self.next.print()
        else:
            connected = "None"
        
        return "{}->{}".format(self, connected)

        ## Iterative
        # cur = self
        # out = ""
        # while cur:
        #     out += str(cur) + "->"
        #     cur = cur.next
        # out += "None"
        # return out


class LinkedList:
    def __init__(self, pylist=[]) -> None:
        self.head = None
        for i in pylist:
            self.append(i)

    def append(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            self._add(self.head, data)

    def _add(self, sub_node, data):
        cur_node = sub_node
        
        while cur_node != None:
            if cur_node.next == None:
                cur_node.next = Node(data)
                return
            cur_node = cur_node.next

    def __str__(self) -> str:
        return ", ".join(str(i.data) for i in self)
    
    def __iter__(self):
        cur_node = self.head
        while cur_node != None:
            yield cur_node
            cur_node= cur_node.next
