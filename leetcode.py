class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        max_m = len(grid[0])
        max_n = len(grid)

        def land_check(m, n):
            grid[n][m] = 0
            if m + 1 < max_m:
                if int(grid[n][m + 1]):
                    land_check(m + 1, n)
                    grid[n][m + 1] = 0
            if n + 1 < max_n:
                if int(grid[n + 1][m]):
                    land_check(m, n + 1)
                    grid[n + 1][m] = 0
            if m - 1 >= 0:
                if int(grid[n][m - 1]):
                    land_check(m - 1, n)
                    grid[n][m - 1] = 0
            if n - 1 >= 0:
                if int(grid[n - 1][m]):
                    land_check(m, n - 1)
                    grid[n - 1][m] = 0
            return 1

        return sum(
            land_check(m, n)
            for n in range(max_n)
            for m in range(max_m)
            if int(grid[n][m])
        )


# Success
# Details
# Runtime: 232 ms, faster than 11.87% of Python3 online submissions for Number of Islands.
# Memory Usage: 14.8 MB, less than 72.79% of Python3 online submissions for Number of Islands.
# ================================================#
#     ^ my answer      ||  most voted answer v   #
# ================================================#


class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.dfs(grid, i, j)
                    count += 1
        return count

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1":
            return
        grid[i][j] = "#"
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)


# ================================================#
#                  question v                     #
# ================================================#

# 200. Number of Islands
# Medium

# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input:
# 11110
# 11010
# 11000
# 00000

# Output: 1
# Example 2:

# Input:
# 11000
# 11000
# 00100
# 00011

# Output: 3
