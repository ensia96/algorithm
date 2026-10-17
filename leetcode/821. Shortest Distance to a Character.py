class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        n = len(s)
        A, p = [n] * n, -n
        for i in range(n):
            if s[i] == c:
                p = i
            A[i] = i - p
        p = 2 * n
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                p = i
            A[i] = min(A[i], p - i)
        return A
