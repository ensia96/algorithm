class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        A, p, c = 0, 0, 1
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                c += 1
            else:
                p, c = c, 1
            A += c <= p
        return A
