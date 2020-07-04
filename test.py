def numIslands(grid):
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
        land_check(m, n) for n in range(max_n) for m in range(max_m) if int(grid[n][m])
    )


# numIslands(
#     [
#         ["1", "1", "1", "1", "0"],
#         ["1", "1", "0", "1", "0"],
#         ["1", "1", "0", "0", "0"],
#         ["0", "0", "0", "0", "0"],
#     ]
# )
numIslands(
    [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
)

print(
    numIslands(
        [
            ["1", "0", "1", "1", "1"],
            ["1", "0", "1", "0", "1"],
            ["1", "1", "1", "0", "1"],
        ]
    )
)

