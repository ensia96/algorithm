# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return (x := +bool(root)) and (min(l := self.minDepth(root.left), r := self.minDepth(root.right)) or max(l, r)) + x
