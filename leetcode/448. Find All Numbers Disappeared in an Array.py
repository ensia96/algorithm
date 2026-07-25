class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            if nums[(j := abs(nums[i]) - 1)] > 0:
                nums[j] = -nums[j]
        return [i + 1 for i in range(n) if nums[i] > 0]
