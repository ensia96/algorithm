# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        A, Q = [], [root] if root else []
        while Q:
            A.append(sum(q.val for q in Q) / len(Q))
            Q = [c for q in Q for c in (q.left, q.right) if c]
        return A
