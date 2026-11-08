class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        e, o, n = 0, 1, len(nums)
        while e < n > o:
            if nums[e] % 2 and not nums[o] % 2:
                nums[e], nums[o] = nums[o], nums[e]
            o += nums[o] % 2 * 2
            e += (not nums[e] % 2) * 2
        return nums
