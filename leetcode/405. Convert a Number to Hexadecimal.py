class Solution:
    def toHex(self, num: int) -> str:
        H = "0123456789abcdef"
        return ''.join(H[num >> i & 15] for i in range(28, -1, -4)).lstrip('0') or '0'
