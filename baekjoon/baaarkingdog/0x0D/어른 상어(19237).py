l, r = lambda: map(int, input().split()), range
n, m, k, e = *l(), [0, (-1, 0), (1, 0), (0, -1), (0, 1)]
b, s, d = [[*l()]for _ in r(n)], [[(0, -1)]*n for _ in r(n)], [0]+[*l()]
p = [0]+[[0]+[[*l()]for _ in r(4)]for _ in r(m)]
for i in r(n*n):
    y, x = i//n, i % n
    b[y][x] = (b[y][x], d[b[y][x]])
for t in r(1000):
    c, h = 0, [0]*(m+1)
    for i in r(n*n):
        y, x = i//n, i % n
        v, w = b[y][x]
        if v:
            s[y][x], h[v], c = (v, t+k), (y, x, w), c+1
    if c == 1:
        exit(print(t))
    for i in r(1, m+1):
        if not h[i]:
            continue
        y, x, d, z = *h[i], []
        for j in p[i][d]:
            ny, nx = y+e[j][0], x+e[j][1]
            if (0 <= ny < n)*(0 <= nx < n):
                z += [[], [(ny, nx, j)]][s[ny][nx][0] == i]
                if s[ny][nx][1] <= t:
                    break
        else:
            ny, nx, j = z[0]
        f, g = b[ny][nx], (b[y][x][0], j)
        b[ny][nx], b[y][x] = [sorted([f, g])[0], g][not f[0]], (0, 0)
print(-1)
