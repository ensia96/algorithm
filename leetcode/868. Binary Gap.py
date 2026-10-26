class Solution:
    def binaryGap(self, n: int) -> int:
        M, l = 0, -1
        for i, b in enumerate(bin(n)):
            if b == '1':
                if l != -1:
                    M = max(M, i - l)
                l = i
        return M
