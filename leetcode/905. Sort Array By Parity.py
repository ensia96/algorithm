class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        e, o = [], []
        for i in nums:
            (o if i % 2 else e).append(i)
        return e + o
