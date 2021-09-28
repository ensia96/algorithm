n, z, c, t = int(input()), 2, 2, 0
m = [[*map(int, input().split())]for _ in range(n)]
for i in range(n*n):
    if m[i//n][i % n] == 9:
        s, m[i//n][i % n] = (i//n, i % n, 0), 0
while 1:
    q, v, f = [s], [0]*n*n, []
    for y, x, d in q:
        for i, j in [(y+1, x), (y-1, x), (y, x+1), (y, x-1)]:
            if 0 <= i < n and 0 <= j < n and m[i][j] <= z and not v[i*n+j]:
                v[i*n+j], f = 1, f+[[], [(d+1, i, j)]][m[i][j] and m[i][j] < z]
                q += [(i, j, d+1)]
    if f:
        d, y, x = sorted(f)[0]
        s, m[y][x], t, c = (y, x, 0), 0, t+d, c-1
        if not c:
            c = z = z+1
        continue
    exit(print(t))
