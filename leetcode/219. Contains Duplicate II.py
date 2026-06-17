class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        D = {}
        for i, j in enumerate(nums):
            if j in D and i - D[j] <= k:
                return True
            D[j] = i
        return False
