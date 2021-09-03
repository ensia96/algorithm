import sys
i, r = sys.stdin.readline, range
n = int(i())
m = [[*map(int, i().split())] for _ in r(n)]
s = [(i, j) for i in r(n) for j in r(n) if m[i][j]]
l = len(s)
a, v = set(), [0] * l
e, f = [0] * (2*n-1), [0] * (2*n-1)


def b(c, p):
    if p == l-1:
        a.add(c)
        return
    for i in r(p, l):
        x, y = s[i]
        if not v[i] and m[x][y] and not e[x+y] and not f[x-y+n-1]:
            v[i], m[x][y], e[x+y], f[x-y+n-1] = 1, 0, 1, 1
            b(c+1, i)
            v[i], m[x][y], e[x+y], f[x-y+n-1] = 0, 1, 0, 0


b(0, 0)
print(max(a))
