class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return (1 << n.bit_length()) + ~n if n else 1
