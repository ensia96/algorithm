i, t, r = input, int, range
v, l = lambda a, b: [
    (a+1, b+2),
    (a+2, b+1),
    (a+2, b-1),
    (a+1, b-2),
    (a-1, b-2),
    (a-2, b-1),
    (a-2, b+1),
    (a-1, b+2)
], lambda: (*map(t, i().split()),)


for _ in r(t(i())):
    n = t(i())
    m = [[0] * n for _ in r(n)]
    a, b = l()
    g = l()
    q = [(a, b)]
    m[a][b] = 1
    for c, d in q:
        if m[g[0]][g[1]]:
            print('answer : ', m[g[0]][g[1]] - 1)
            break
        for x, y in v(c, d):
            if 0 <= x < n and 0 <= y < n and not m[x][y]:
                m[x][y] = m[c][d] + 1
                q += [(x, y)]
