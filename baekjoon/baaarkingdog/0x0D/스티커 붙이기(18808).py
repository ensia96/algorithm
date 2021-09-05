import sys

i = sys.stdin.readline
l, g = lambda: map(int, i().split()), range
n, m, k = l()
b = [[0]*m for _ in g(n)]


def t(r, c):
    a = [[0] * r for _ in g(c)]
    for u in g(c):
        for v in g(r):
            a[u][v] = p[r-1-v][u]
    return c, r, a


def e(x, y):
    if not any(b[x+u][y+v] and p[u][v] for u in g(r) for v in g(c)):
        for u in g(r):
            for v in g(c):
                if p[u][v]:
                    b[x+u][y+v] = 1
        return 1


while k:
    k -= 1
    r, c = l()
    p = [[*l()] for __ in g(r)]
    for _ in g(4):
        if any(e(x, y) for x in g(n-r+1) for y in g(m-c+1)):
            break
        r, c, p = t(r, c)

print(sum(sum(l) for l in b))
