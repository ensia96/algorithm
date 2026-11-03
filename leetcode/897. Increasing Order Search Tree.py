# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode | None) -> TreeNode | None:
        A = c = TreeNode()

        def f(x):
            nonlocal c
            if not x:
                return
            f(x.left)
            c.right = x
            x.left = None
            c = x
            f(x.right)
        f(root)
        c.right = None
        return A.right
