class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        y = x = sum(nums[:k])
        return max([y] + [x := x + nums[i + k] - nums[i] for i in range(len(nums) - k)]) / k
