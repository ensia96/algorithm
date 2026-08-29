class Solution:
    def findLHS(self, nums: List[int]) -> int:
        import collections
        C = collections.Counter(nums)
        return max(int(c + 1 in C) and C[c] + C[c + 1] for c in C)
