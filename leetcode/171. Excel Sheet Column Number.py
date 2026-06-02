class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        A = 0
        for i in columnTitle:
            A = A * 26 + ord(i) - 64
        return A
