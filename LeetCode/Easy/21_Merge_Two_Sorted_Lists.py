"""
21. MERGE TWO SORTED LISTS
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
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
iterate over both LLists
1. set list3 and head node
2. iterate over each list
3. at the end of while, attach the 
rest of the remaining list to list3
"""
def mergeTwoLists(list1, list2):
    list3 = head = ListNode()
    while list1 and list2:
        if list1.val < list2.val:
            list3.next = list1
            list3 = list3.next
            list1 = list1.next
        else:
            list3.next = list2
            list3 = list3.next
            list2 = list2.next
    if list1 or list2:
        list3.next = list1 if list1 else list2
    return head.next
    
if __name__ == "__main__":
    list1 = LList([1,2,3,5,6])
    list2 = LList([1,3,4])
    list3 = mergeTwoLists(list1,list2)
    cur = list3
    s = ""
    while cur:
        s  = s + str(cur.val)
        cur = cur.next
    print(s)