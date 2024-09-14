"""
141. LINKED LIST CYCLE
Given head, the head of a linked list, determine
if the linked list has a cycle in it.

There is a cycle in a linked list if there is some
node in the list that can be reached again by continuously
following the next pointer. Internally, pos is used to
denote the index of the node that tail's next pointer is
connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list.
Otherwise, return false.
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


"""
first solution:
(29ms/89.05%)(20.21MB/77.84%)
Floyd's Cycle Algorithm
1. have a pointer that increments by one
and another that increments by two
2. if there is a cycle, eventually the two
pointers will overlap
"""


def hasCycle(head):
    if not head.next:
        return False
    f = head
    l = head
    while l.next and l.next.next:
        f = f.next
        l = l.next.next
        if f == l:
            return True
    return False


if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node5
    print(hasCycle(node1))
