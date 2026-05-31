class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        A = ''
        while columnNumber > 0:
            columnNumber -= 1
            A += chr(columnNumber % 26 + 65)
            columnNumber //= 26
        return A[::-1]
