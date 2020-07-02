class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        return False


# ================================================#
#     ^ my answer      ||  most voted answer v   #
# ================================================#


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        max_path = float("-inf")

        def get_max_gain(node):
            nonlocal max_path
            if node is None:
                return 0

            gain_on_left = max(get_max_gain(node.left), 0)
            gain_on_right = max(get_max_gain(node.right), 0)

            current_max_path = node.val + gain_on_left + gain_on_right
            max_path = max(max_path, current_max_path)

            return node.val + max(gain_on_left, gain_on_right)

        get_max_gain(root)
        return max_path


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
