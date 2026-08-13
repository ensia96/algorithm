class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        return -(a == b) or max(len(a), len(b))
