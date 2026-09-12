class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        x = sum(nums[:k])
        return max((x := x + nums[i + k] - nums[i] for i in range(len(nums) - k)), default=x) / k
