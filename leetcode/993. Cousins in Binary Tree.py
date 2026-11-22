# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode | None, x: int, y: int) -> bool:
        S = [(root, 0, None)]
        X = Y = None
        while S and not (X and Y):
            N, d, P = S.pop()
            if N.val == x:
                X = (d, P)
            if N.val == y:
                Y = (d, P)
            if N.right:
                S.append((N.right, d + 1, N))
            if N.left:
                S.append((N.left, d + 1, N))
        return X[0] == Y[0] and X[1] != Y[1]
