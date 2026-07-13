class Solution:
    def firstUniqChar(self, s: str) -> int:
        from collections import Counter
        C = Counter(s)
        return next((i for i, c in enumerate(s) if C[c] == 1), -1)
