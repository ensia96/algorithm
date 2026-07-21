class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        A = []
        for n in nums:
            A = sorted({*A, n})[-3:]
        return A[-(len(A) < 3)]
