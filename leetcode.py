class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return [_ for _ in set(nums) if nums.count(_) == 1][0]


# Success
# Details
# Runtime: 5408 ms, faster than 6.85% of Python3 online submissions for Single Number.
# Memory Usage: 16.2 MB, less than 73.89% of Python3 online submissions for Single Number.
# ================================================#
#     ^ my answer      ||  most voted answer v   #
# ================================================#


class Solution:
    def singleNumber1(self, nums):
        dic = {}
        for num in nums:
            dic[num] = dic.get(num, 0) + 1
        for key, val in dic.items():
            if val == 1:
                return key

    # def singleNumber2(self, nums):
    #     res = 0
    #     for num in nums:
    #         res ^= num
    #     return res

    # def singleNumber3(self, nums):
    #     return 2*sum(set(nums))-sum(nums)

    # def singleNumber4(self, nums):
    #     return reduce(lambda x, y: x ^ y, nums)

    # def singleNumber(self, nums):
    #     return reduce(operator.xor, nums)


# ================================================#
#                  question v                     #
# ================================================#

# 124. Binary Tree Maximum Path Sum
# Hard

# Given a non-empty binary tree, find the maximum path sum.

# For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

# Example 1:

# Input: [1,2,3]

#        1
#       / \
#      2   3

# Output: 6
# Example 2:

# Input: [-10,9,20,null,null,15,7]

#    -10
#    / \
#   9  20
#     /  \
#    15   7

# Output: 42

# TreeNode{val: 1, left: TreeNode{val: 2, left: None, right: None}, right: TreeNode{val: 3, left: None, right: None}}
