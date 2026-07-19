class Solution:
    def longestPalindrome(self, s: str) -> int:
        from collections import Counter
        return len(s) - (S := sum(i % 2 for i in Counter(s).values())) + bool(S)
