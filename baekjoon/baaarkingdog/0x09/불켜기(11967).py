import sys
i, r = sys.stdin.readline, range
l, d, q = lambda: map(int, i().split()), {}, [(1, 1)]
n, m = l()
g, v = [[0] * (n+1) for _ in r(n+1)], [[0] * (n+1) for _ in r(n+1)]
g[1][1] = 1

for _ in r(m):
    x, y, a, b = l()
    c = x, y
    if c not in d:
        d[c] = []
    d[c].append((a, b))

for m in q:
    if m in d:
        for x, y in d[m]:
            g[x][y] = 1
    a, b = m
    for x, y in [(a+1, b), (a-1, b), (a, b+1), (a, b-1)]:
        if 0 < x <= n and 0 < y <= n and g[x][y] and not v[x][y]:
            q += [(x, y)]
            v[x][y] = 1

print(sum(sum(g[i]) for i in r(n+1)))
