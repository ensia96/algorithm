import sys
sys.setrecursionlimit(10**6)
i, r = sys.stdin.readline, range
l, d = lambda: map(int, i().split()), {}
n, m = l()
g = [[0] * (n+1) for _ in r(n+1)]
g[1][1] = 1

for _ in r(m):
    x, y, a, b = l()
    c = x, y
    if c not in d:
        d[c] = []
    d[c].append((a, b))


def c(s, f):
    q, v = [s], []
    for m in q:
        if m in d:
            for x, y in d.pop(m):
                g[x][y] = 1
                c((x, y), (1, 1))
        a, b = m
        for x, y in [(a+1, b), (a-1, b), (a, b+1), (a, b-1)]:
            if 0 < x <= n and 0 < y <= n and g[x][y] and (x, y) not in v:
                if (x, y) == f:
                    return
                q += [(x, y)]
                v += [(x, y)]


c((1, 1), None)

print(sum(sum(g[i]) for i in r(n+1)))
