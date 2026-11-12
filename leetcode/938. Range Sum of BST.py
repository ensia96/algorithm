# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode | None, low: int, high: int) -> int:
        return +bool(root) and ((low <= root.val <= high) * root.val + (low < root.val and self.rangeSumBST(root.left, low, high)) + (root.val < high and self.rangeSumBST(root.right, low, high)))
