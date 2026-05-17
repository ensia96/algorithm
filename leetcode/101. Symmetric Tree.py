# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isMirror(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        return left and right and left.val == right.val and self.isMirror(left.left, right.right) and self.isMirror(left.right, right.left) or not left and not right

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return not root or self.isMirror(root.left, root.right)
