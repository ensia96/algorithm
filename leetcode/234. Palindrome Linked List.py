# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        i, j, k = head, head, None
        while j and j.next:
            i, j = i.next, j.next.next
        while i:
            i.next, k, i = k, i, i.next
        while k and head.val == k.val:
            head, k = head.next, k.next
        return not k
