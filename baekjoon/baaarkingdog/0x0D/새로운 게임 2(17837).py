l, r = lambda: map(int, input().split()), range
n, k = l()
b, m = [[*l()]for _ in r(n)], [[[]for _ in r(n)]for _ in r(n)]
e, o = lambda y, x: (0 <= y < n)*(0 <= x < n)-1 or b[y][x] == 2, []
for i in r(k):
    y, x, d = l()
    m[y-1][x-1] += [i]
    o += [(y-1, x-1, d-1)]
for t in r(1000):
    for i in r(k):
        y, x, d = o[i]
        c, v = m[y][x], [(y, x+1), (y, x-1), (y-1, x), (y+1, x)]
        h = c.index(i)
        u, ny, nx = c[h:], *v[d]
        d = [d, (d//2)*2+[1, 0][d % 2]][e(ny, nx)]
        ny, nx, o[i] = *v[d], (y, x, d)
        if e(ny, nx):
            continue
        u = u[::[1, -1][b[ny][nx] == 1]]
        m[y][x], m[ny][nx] = c[:h], m[ny][nx]+u
        if len(m[ny][nx]) > 3:
            exit(print(t+1))
        for p in u:
            o[p] = (ny, nx, o[p][2])
print(-1)
