class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)


# Success
# Details
# Runtime: 72 ms, faster than 46.50% of Python3 online submissions for Maximum Subarray.
# Memory Usage: 14.8 MB, less than 10.99% of Python3 online submissions for Maximum Subarray.

# ================================================#
#     ^ my answer      ||  most voted answer v   #
# ================================================#


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        from itertools import accumulate

        return max(accumulate(nums, lambda x, y: x + y if x > 0 else y))


# ================================================#
#                  question v                     #
# ================================================#

# 53. Maximum Subarray
# Easy

# Add to List

# Share
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:

# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
