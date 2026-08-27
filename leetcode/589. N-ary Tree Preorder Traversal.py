"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        A, I = [], [root]
        while I:
            i = I.pop()
            A.append(i.val)
            I.extend(reversed(i.children))
        return A
