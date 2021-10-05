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


for p in t.permutations(a, 5):
    m = [[[o[k][j][i]for i in a]for j in a]for k in p]
    for f0 in f:
        u = l(m[0])
        if f0*(u == m[0]):
            continue
        m[0] = u
        if u[0][0]:
            for f1 in f:
                u = l(m[1])
                if f1*(u == m[1]):
                    continue
                m[1] = u
                for f2 in f:
                    u = l(m[2])
                    if f2*(u == m[2]):
                        continue
                    m[2] = u
                    for f3 in f:
                        u = l(m[3])
                        if f3*(u == m[3]):
                            continue
                        m[3] = l(m[3])
                        for f4 in f:
                            u = l(m[4])
                            if f4*(u == m[4]):
                                continue
                            m[4] = u
                            if u[4][4]:
                                n = s(n)

print([n, -1][n == 10**5])
