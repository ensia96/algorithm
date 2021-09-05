import sys

i = sys.stdin.readline
l, g = lambda: map(int, i().split()), range
n, m, k = l()
b = [[0]*m for _ in g(n)]
s, t = [], []


def h(f, r, c):
    a = [[] for _ in g(4)]
    q = [a[q].append([(i, j), (j, r-1-i), (r-1-i, c-1-j), (c-1-j, i)][q])
         for q in g(4) for i in g(r) for j in g(c) if f[i][j]]
    return a


def u(f, e, d, r, c):
    for i in g(4):
        if all(0 <= y+e < n and 0 <= x+d < m and not b[y+e][x+d] for y, x in f[i]):
            for y, x in f[i]:
                b[y+e][x+d] = 1
            return 1
    if not(d or e):
        r = max(n, m)
        for i in g(r):
            for j in g(r):
                if i+j > 0:
                    if u(f, e+i, d+j, r, c):
                        return


for _ in g(k):
    r, c = l()
    s, t = s+[(r, c)], t + [[[*l()] for __ in g(r)]]

t = [h(t[i], *s[i]) for i in g(k)]
t = [u(t[p], 0, 0, *s[p]) for p in g(k)]
print(sum(sum(l) for l in b))
