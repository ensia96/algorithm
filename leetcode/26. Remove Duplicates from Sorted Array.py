class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        S = {*nums}
        nums[:] = sorted(S)
        return len(S)
