class Solution:
    def largestSumAfterKNegations(self, nums: list[int], k: int) -> int:
        A = sum(nums)
        if k == 1:
            return A - 2 * min(nums)
        from collections import Counter
        C = Counter(nums)
        for i in range(-100, 0):
            f = min(k, C[i])
            A -= 2 * i * f
            k -= f
            if k == 0:
                return A
        return A - 2 * min(map(abs, C)) if k % 2 else A
