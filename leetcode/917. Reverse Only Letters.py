class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        L = [*filter(str.isalpha, s)]
        return ''.join(L.pop()if c.isalpha()else c for c in s)
