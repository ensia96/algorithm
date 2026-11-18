# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode | None) -> bool:
        S, v = [root], root.val
        while S:
            i = S.pop()
            if i.val != v:
                return False
            if i.right:
                S.append(i.right)
            if i.left:
                S.append(i.left)
        return True
