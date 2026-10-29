class Solution:
    def projectionArea(self, grid: list[list[int]]) -> int:
        N = range(len(grid))
        return sum(grid[i][j] > 0 for i in N for j in N) + sum(max(row) for row in grid) + sum(max(grid[i][j] for i in N) for j in N)
