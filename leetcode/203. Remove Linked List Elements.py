# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        A = ListNode()
        A.next = head
        i = A
        while i.next:
            if i.next.val == val:
                i.next = i.next.next
            else:
                i = i.next
        return A.next
