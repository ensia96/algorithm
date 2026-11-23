class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        if len(trust) < n - 1:
            return -1
        S = [0] * (n + 1)
        for a, b in trust:
            S[a] -= 1
            S[b] += 1
        try:
            return S.index(n - 1, 1)
        except ValueError:
            return -1
