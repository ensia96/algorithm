import itertools as t
import collections as c
e, g = lambda x: 0 <= x < 5, range
b, a, f = lambda a, b, c: a*5*5+b*5+c, g(5), g(4)
o = [[[*map(int, input().split())]for _ in a]for _ in a]
l, n = lambda f: [[f[4-j][i]for j in a]for i in a], 10**5


def s(n):
    q, v = c.deque([(0, 0, 0)]), [0]*5**3
    while q:
        x, y, z = q.popleft()
        for i, j, k in [(x+1, y, z), (x-1, y, z), (x, y+1, z), (x, y-1, z), (x, y, z+1), (x, y, z-1)]:
            if e(i)*e(j)*e(k) and m[k][j][i]*(not v[b(k, j, i)]):
                if i*j*k == 4**3:
                    return min(v[b(z, y, x)]+1, n)
                v[b(k, j, i)] = v[b(z, y, x)]+1
                q += [(i, j, k)]
    return n


def h(i, n):
    if i == 5:
        return s(n)
    for j in f:
        u = l(m[i])
        if j*(u == m[i]):
            continue
        m[i] = u
        if (i == 0)*(not u[0][0]) or (i == 4)*(not u[4][4]):
            continue
        n = h(i+1, n)
    return n


for p in t.permutations(a, 5):
    m = [[[o[k][j][i]for i in a]for j in a]for k in p]
    n = h(0, n)

print([n, -1][n == 10**5])
