class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        x = 0
        return max(x := (x + 1) * i for i in nums)
