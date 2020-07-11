class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = nums.count(0)
        while 0 in nums:
            nums.remove(0)
        for i in range(zeros):
            nums.append(0)


# Success
# Details
# Runtime: 188 ms, faster than 15.92% of Python3 online submissions for Move Zeroes.
# Memory Usage: 15.1 MB, less than 16.48% of Python3 online submissions for Move Zeroes.
# ================================================#
#     ^ my answer      ||  most voted answer v   #
# ================================================#


class Solution:
    def moveZeroes(self, nums):
        for i in range(len(nums))[::-1]:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)


# ================================================#
#                  question v                     #
# ================================================#

# 283. Move Zeroes
# Easy

# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
