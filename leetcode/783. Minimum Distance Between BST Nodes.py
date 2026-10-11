# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode | None) -> int:
        self.p = None
        self.m = 10**5

        def f(x):
            if not x:
                return
            f(x.left)
            if self.p is not None:
                self.m = min(self.m, x.val - self.p)
            self.p = x.val
            f(x.right)
        f(root)
        return self.m
