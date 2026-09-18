class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        t = 1
        return max((t := t * (nums[i] < nums[i + 1]) + 1 for i in range(len(nums) - 1)), default=1)
