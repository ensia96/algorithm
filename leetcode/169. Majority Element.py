class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c, t = 0, None
        for n in nums:
            if c == 0:
                t = n
            c += 2 * (n == t) - 1
        return t
