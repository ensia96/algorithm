# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        a, *A = [-1, root]
        while A:
            if (i := A.pop()).left:
                for j in (i.left, i.right):
                    if j.val == i.val:
                        A.append(j)
                    else:
                        a = j.val if a == -1 else min(a, j.val)
        return a
