# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return bool(root) and (self.f(root, subRoot) or (self.isSubtree(
            root.left, subRoot) or self.isSubtree(root.right, subRoot)))

    def f(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return bool(not p and not q) or bool(p and q and p.val == q.val and self.f(
            p.left, q.left) and self.f(p.right, q.right))
