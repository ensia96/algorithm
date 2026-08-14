# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.p = None
        self.m = 10**5

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.p is not None:
                self.m = min(self.m, node.val - self.p)
            self.p = node.val
            inorder(node.right)
        inorder(root)
        return self.m
