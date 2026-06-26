# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> list[str]:
        return ['->'.join([str(root.val), p]) for p in self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right)] or [str(root.val)]if root else []
