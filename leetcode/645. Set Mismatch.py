class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n, s = len(nums), sum(nums)
        return [x := s - sum(set(nums)), n * (n + 1) // 2 - s + x]
