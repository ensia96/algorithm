class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        return sum(
            1
            for i in range(len(nums))
            for j in range(1, len(nums) + 1)
            if i < j and sum(nums[i:j]) == k
        )


#
#
#
#
# ================================================#
#     ^ my answer      ||  most voted answer v   #
# ================================================#


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sums = 0
        d = dict()
        d[0] = 1

        for i in range(len(nums)):
            sums += nums[i]
            count += d.get(sums - k, 0)
            d[sums] = d.get(sums, 0) + 1

        return count


# ================================================#
#                  question v                     #
# ================================================#

# 543. Diameter of Binary Tree
# Easy

# Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

# Example:
# Given a binary tree
#           1
#          / \
#         2   3
#        / \
#       4   5
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

# Note: The length of path between two nodes is represented by the number of edges between them.
