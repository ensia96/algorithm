# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode | None, root2: TreeNode | None) -> bool:
        def f(x, L) -> None:
            if not x:
                return
            if not x.left and not x.right:
                L.append(x.val)
            f(x.left, L)
            f(x.right, L)
        A = []
        B = []
        f(root1, A)
        f(root2, B)
        return A == B
