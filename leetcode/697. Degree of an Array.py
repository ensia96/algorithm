class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        D = {}
        for i, x in enumerate(nums):
            if x not in D:
                D[x] = [0, i, i]
            D[x][0] += 1
            D[x][1] = i
        return min((-i, j - k + 1) for i, j, k in D.values())[1]
