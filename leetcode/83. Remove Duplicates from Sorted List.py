# Definition for singly-linked list.
# from typing import Optional
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        N = head
        while N and N.next:
            if N.val == N.next.val:
                N.next = N.next.next
            else:
                N = N.next
        return head
