a, r = 0, range
g, b = [[0]*4 for _ in r(10)], [[0]*4 for _ in r(10)]


def f(a, m):
    for p in r(39, 3, -1):
        i, j, t = p//4-1, p % 4, 1
        if m[i+1][j]+(not m[i][j]):
            continue
        l = [(i, j)]+[(y, x)for y, x in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
                      if (0 <= y < 10)*(0 <= x < 4) and m[y][x] == m[i][j]]
        while t:
            t = []
            if all(y < 9 and m[y+1][x] in [0, m[y][x]]for y, x in l):
                for y, x in l:
                    m[y+1][x], m[y][x] = m[y][x], m[y+1][x]
                    t += [(y+1, x)]
            l = t
        for i, j in [(all(m[i]), i)for i in r(10)]:
            a, m[j] = a+i, [m[j], [0]*4][i]
            if i:
                a, m = f(a, m)
                break
    l = sum(any(m[i])for i in r(4, 6))
    m = [[0]*4 for _ in r(l)]+m[:10-l]
    return a, m


for _ in r(int(input())):
    t, y, x = map(int, input().split())
    g[y][x] = b[x][3-y] = _+1
    if t > 1:
        i, j, k = [(y, x+1, 3-y), (y+1, x, 2-y)][t-2]
        g[i][j] = b[j][k] = _+1
    a, g = f(a, g)
    a, b = f(a, b)
print(a)
print(32-sum(b[i].count(0)+g[i].count(0)for i in r(6, 10)))
