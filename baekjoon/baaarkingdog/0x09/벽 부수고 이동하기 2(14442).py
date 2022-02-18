n, m, k = map(int, input().split())
B = [[*map(int, input())]for _ in ' '*n]
D, d = [[0]*m for _ in ' '*n], 1
D[0][0], Q = 1, [(0, 0, k)]
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
                D[x][y] = z
                q += (x, y, z),
    Q, d = q, d+1
print(-1)
