l, r = lambda: map(int, input().split()), range
n, k = l()
b, m = [[*l()]for _ in r(n)], [[[]for _ in r(n)]for _ in r(n)]
e, o = lambda y, x: (0 <= y < n)*(0 <= x < n)-1 or b[y][x] == 2, []
for i in r(k):
    y, x, d = l()
    m[y-1][x-1] += [i]
    o += [[y-1, x-1, d-1]]
for t in r(1000):
    for i in r(k):
        y, x, d = o[i]
        c, v = m[y][x], [(y, x+1), (y, x-1), (y-1, x), (y+1, x)]
        d = [d, (d//2)*2+[1, 0][d % 2]][e(*v[d])]
        p, q, o[i][2] = *v[d], d
        if e(p, q):
            continue
        h = c.index(i)
        u = c[h:][::[1, -1][b[p][q] == 1]]
        m[y][x], m[p][q] = c[:h], m[p][q]+u
        if len(m[p][q]) > 3:
            exit(print(t+1))
        o = [[o[_], [p, q, o[_][2]]][_ in u]for _ in r(k)]
print(-1)
