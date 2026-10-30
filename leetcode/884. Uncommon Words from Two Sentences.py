class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> list[str]:
        from collections import Counter
        C = Counter(A.split())
        C.update(B.split())
        return [w for w, n in C.items() if n == 1]
