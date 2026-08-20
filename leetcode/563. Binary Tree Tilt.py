# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.t = 0

        def f(x):
            if not x:
                return 0
            l, r = f(x.left), f(x.right)
            self.t += abs(l - r)
            return l + r + x.val
        f(root)
        return self.t
