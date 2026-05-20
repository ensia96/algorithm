# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node):
            return +bool(node) and (-((l := check(node.left)) < 0 or (r := check(node.right)) < 0 or abs(l - r) > 1) or 1 + max(l, r))
        return check(root) >= 0
