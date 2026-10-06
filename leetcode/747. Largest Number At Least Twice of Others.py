class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 0
        M = max(nums)
        I = nums.index(M)
        for i in range(len(nums)):
            if i != I and nums[i] * 2 > M:
                return -1
        return I
