n, m, k = map(int, input().split())
B = [[*map(int, input())]for _ in ' '*n]
D = [[-1]*m for _ in ' '*n]
d = s = 1
Q = [(0, 0, k)]
while Q:
    q = []
    for i, j, h in Q:
        if (i, j) == (n-1, m-1):
            exit(print(d))
        for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if not (0 <= x < n)*(0 <= y < m):
                continue
            z = h-B[x][y]
            if D[x][y] < z:
                if B[x][y] and not s:
                    x, y, z = i, j, z+1
                D[x][y] = z
                q += (x, y, z),
    d, s, Q = d+1, not s, q
print(-1)
