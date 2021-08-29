i, r = input, range
n = int(i())
m, s = [[*i()] for _ in r(n)], 'RG'

c, v = 0, [[0] * n for _ in r(n)]
d, w = 0, [[0] * n for _ in r(n)]


def p(a, b, c, d):
    q, v[a][b] = [(a, b)], 1
    for i, j in q:
        for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
            if 0 <= x < n and 0 <= y < n and not d[x][y] and m[x][y] in c:
                d[x][y] = 1
                q += [(x, y)]


for i in r(n):
    for j in r(n):
        if not v[i][j]:
            c += 1
            p(i, j, m[i][j], v)
        if not w[i][j]:
            t = m[i][j]
            d += 1
            p(i, j, s if t in s else t, w)

print(c, d)
