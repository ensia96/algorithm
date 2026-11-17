class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        S = set()
        for i in nums:
            if i in S:
                return i
            S.add(i)
