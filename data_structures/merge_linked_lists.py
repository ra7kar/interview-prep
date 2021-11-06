# merge sorted linked lists

import linked_list as ll


def merge_lists(l1, l2):
    out = ll.LinkedList()

    l1_cur = l1.head
    l2_cur = l2.head

    while l1_cur or l2_cur:
        if l1_cur is None:
            # L1 is done
            out.append(l2_cur.data)
            l2_cur = l2_cur.next
        elif l2_cur is None or l1_cur.data <= l2_cur.data:
            # L2 is done or L1 is smaller than L2
            out.append(l1_cur.data)
            l1_cur = l1_cur.next
        else:
            # L2 is smaller than or equal to L1
            out.append(l2_cur.data)
            l2_cur = l2_cur.next

    return out


llist2 = ll.LinkedList([10, 10, 12])
llist1 = ll.LinkedList([1, 10, 10, 12])
# llist = ll.LinkedList([5,7,8,11,30,40])
print(merge_lists(llist1, llist2))
