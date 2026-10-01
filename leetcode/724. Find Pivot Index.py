class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        c, t = 0, sum(nums)
        for i, x in enumerate(nums):
            t -= x
            if c == t:
                return i
            c += x
        return -1
