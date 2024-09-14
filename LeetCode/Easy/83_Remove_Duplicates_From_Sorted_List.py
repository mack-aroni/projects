"""
83. REMOVE DUPLICATES FROM SORTED LIST
Given the head of a sorted linked list, delete
all duplicates such that each element appears only
once. Return the linked list sorted as well.
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def LList(list):
    temp = cur = ListNode()
    for i in list:
        cur.next = ListNode(i)
        cur = cur.next
    head = temp.next
    return head


"""
first solution:
(22ms/74.93%)(13.43%/23.15%)
pointer jumping
1. remove base case(empty list)
2. assign dummy head, first index, and iterator
3. iterate over the list from the second index
4. if the current index is different from value,
make cur temp.next and reassign value and temp
5. at the end, if temp != cur node, cut off the list
"""


def deleteDuplicates(head):
    if not head:
        return None
    temp = head
    value = head.val
    cur = head.next
    while cur != None:
        if cur.val != value:
            temp.next = cur
            value = cur.val
            temp = cur
        cur = cur.next
    if temp != cur:
        temp.next = None
    return head


"""
second solution:
(24ms/62.90%)(13.28MB/84.99%)
iterative
1. iterate over the list
2. if the next value is the same as the current value,
skip over the next index, continue until if statement 
is false
"""


def deleteDuplicates_2(head):
    temp = head
    while temp and temp.next:
        if temp.next.val == temp.val:
            temp.next = temp.next.next
            continue  # continue works until if statement is false
        temp = temp.next
    return head


if __name__ == "__main__":
    list = LList([1, 1, 2, 3, 3])
    head = deleteDuplicates(list)
    cur = head
    s = ""
    while cur:
        s = s + str(cur.val)
        cur = cur.next
    print(s)

    list2 = LList([1, 1])
    head2 = deleteDuplicates(list2)
    cur = head2
    s = ""
    while cur:
        s = s + str(cur.val)
        cur = cur.next
    print(s)
