class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r and s[l] == s[r]:
            l, r = l + 1, r - 1
        f = lambda i, j: all(s[i + d] == s[j - d]
                             for d in range((j - i + 1) // 2))
        return l >= r or f(l + 1, r) or f(l, r - 1)
