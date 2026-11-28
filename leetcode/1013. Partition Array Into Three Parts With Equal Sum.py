class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        T = sum(arr)
        if T % 3:
            return False
        from itertools import accumulate
        T //= 3
        P = accumulate(arr)
        return T in P and 2 * T in P and next(P, None) is not None
