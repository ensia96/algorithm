class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        s, n = 0, len(nums)
        return [['->'.join(map(str, [nums[s]] + [nums[i]] * (s != i))), s := i + 1][0]
                for i in range(n) if i + 1 == n or nums[i + 1] != nums[i] + 1]
