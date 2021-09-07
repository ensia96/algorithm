import sys
l, r = lambda: map(int, sys.stdin.readline().split()), range
n, m = l()
b, d = [[*l()]for _ in r(n)], [[-1]*m for _ in r(n)]


def f(y, x):
    if (y, x) == (n-1, m-1):
        return 1
    d[y][x] = 0
    for i, j in [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]:
        if (0 <= i < n)*(0 <= j < m) and b[i][j] < b[y][x]:
            d[y][x] += d[i][j]if d[i][j]+1 else f(i, j)
    return d[y][x]


print(f(0, 0))
