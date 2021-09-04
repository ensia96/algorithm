a, r = 0, range
g, b = [[0]*4 for _ in r(10)], [[0]*4 for _ in r(10)]


def f(a, l, m):
    t = l
    while t:
        t = []
        if all(y < 9 and m[y+1][x] in [0, m[y][x]]for y, x in l):
            for y, x in l:
                m[y+1][x], m[y][x] = m[y][x], m[y+1][x]
                t += [(y+1, x)]
        l = t
    for i in r(10):
        if all(m[i]):
            a, m = a+1, [[0]*4]+m[:i]+m[i+1:]
    l = sum(any(m[i])for i in r(4, 6))
    m = [[0]*4 for _ in r(l)]+m[:10-l]
    return a, m


for _ in r(int(input())):
    t, y, x = map(int, input().split())
    g[y][x] = b[x][3-y] = _+1
    p, q = [(y, x)], [(x, 3-y)]
    if t > 1:
        i, j, k = [(y, x+1, 3-y), (y+1, x, 2-y)][t-2]
        g[i][j] = b[j][k] = _+1
        p, q = [(i, j)]+p, [(j, k)]+q
    a, g = f(a, p, g)
    a, b = f(a, q, b)
print(a)
print(32-sum(b[i].count(0)+g[i].count(0)for i in r(6, 10)))
