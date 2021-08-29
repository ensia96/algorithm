import sys

i = sys.stdin.readline
n, m = map(int, i().split())
t, q = [[0] * m for _ in range(n)], [(0, 0, 0)]
b = [[*map(int, [*i().strip()])] for _ in range(n)]
b[0][0] = 1

for i, j, f in q:
    for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
        if 0 <= x < n and 0 <= y < m:
            if b[x][y] == 1 and not f:
                b[x][y] = b[i][j] + 1
                q += [(x, y, 1)]
            if not b[x][y]:
                b[x][y] = b[i][j] + 1
                q += [(x, y, f)]

a = b[n - 1][m - 1]
print(a if a else -1)
