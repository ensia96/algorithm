class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        x = y = 1
        for i in range(1, len(nums)):
            y &= nums[i] >= nums[i - 1]
            x &= nums[i] <= nums[i - 1]
        return bool(x or y)
