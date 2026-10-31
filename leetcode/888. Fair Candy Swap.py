class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        s, S = (sum(aliceSizes) - sum(bobSizes)) // 2, set(bobSizes)
        for x in aliceSizes:
            if x - s in S:
                return [x, x - s]
