class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        return 2 * sum(grid[r][c] * (2 - (r > 0 and grid[r - 1][c] == 1) - (c > 0 and grid[r][c - 1] == 1)) for r in range(len(grid)) for c in range(len(grid[0])))
