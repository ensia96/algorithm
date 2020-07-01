class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid) - 1
        column = len(grid[0]) - 1
        i = row - 1
        j = column - 1

        while j >= 0:
            grid[row][j] += grid[row][j + 1]
            j -= 1

        while i >= 0:
            grid[i][column] += grid[i + 1][column]
            i -= 1

        j = column - 1
        i = row - 1

        while i >= 0:
            while j >= 0:
                grid[i][j] += min(grid[i][j + 1], grid[i + 1][j])
                j -= 1
            j = column - 1
            i -= 1
        return grid[0][0]


# Success
# Details
# Runtime: 92 ms, faster than 97.66% of Python3 online submissions for Minimum Path Sum.
# Memory Usage: 15.3 MB, less than 54.27% of Python3 online submissions for Minimum Path Sum.
# ================================================#
#     ^ my answer      ||  most voted answer v   #
# ================================================#


class Solution:
    def minPathSum(self, grid):
        M, N = len(grid), len(grid[0])
        dp = [0] + [sys.maxint] * (N - 1)
        for i in range(M):
            dp[0] = dp[0] + grid[i][0]
            for j in range(1, N):
                dp[j] = min(dp[j - 1], dp[j]) + grid[i][j]
        return dp[-1]


# ================================================#
#                  question v                     #
# ================================================#

# 64. Minimum Path Sum
# Medium

# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

# Note: You can only move either down or right at any point in time.

# Example:

# Input:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.
