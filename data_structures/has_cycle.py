# check if llist has a cyclic link.

from linked_list import LinkedList


def has_cycle(llist):
    # cur_node = llist.head
    # seen = set()
    # while cur_node is not None:

    #     if id(cur_node) in seen:
    #         return 1
    #     seen.add(id(cur_node))
    #     cur_node = cur_node.next

    # return 0

    cur_node1 = llist.head
    cur_node2 = llist.head.next.next

    while cur_node1 is not None or cur_node2 is not None:

        cur_node1 = cur_node1.next
        if cur_node2.next is not None:
            cur_node2 = cur_node2.next.next
        else:
            cur_node2 = None

        if cur_node1 is None or cur_node2 is None:
            return 0

        if id(cur_node1) == id(cur_node2):
            return 1

    return 0


llist = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9])
# llist.head.next.next.next.next.next.next.next.next = llist.head
# print(llist)
print("_______Result________")
res = has_cycle(llist)
print(res)
