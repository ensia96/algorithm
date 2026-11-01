class Solution:
    def surfaceArea(self, grid: list[list[int]]) -> int:
        A = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    A += 2 + 4 * grid[i][j]
                    if i > 0:
                        A -= min(grid[i][j], grid[i - 1][j]) * 2
                    if j > 0:
                        A -= min(grid[i][j], grid[i][j - 1]) * 2
        return A
