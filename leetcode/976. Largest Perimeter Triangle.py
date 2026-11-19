class Solution:
    def largestPerimeter(self, nums: list[int]) -> int:
        *S, i, j, k = sorted(nums)
        while (f := i + j <= k) and S:
            i, j, k = S.pop(), i, j
        return (f ^ 1) * (i + j + k)
