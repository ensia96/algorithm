# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        A, S = set(), [root] if root else []
        while S:
            s = S.pop()
            if k - s.val in A:
                return True
            A.add(s.val)
            if s.right:
                S.append(s.right)
            if s.left:
                S.append(s.left)
        return False
