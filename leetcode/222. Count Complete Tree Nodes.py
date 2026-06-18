# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        return +bool(root) and ((l := self.d(root.left)) == (r := self.d(root.right)) and (1 << l) + self.countNodes(root.right) or (1 << r) + self.countNodes(root.left))

    def d(self, n):
        d = 0
        while n:
            d += 1
            n = n.left
        return d
