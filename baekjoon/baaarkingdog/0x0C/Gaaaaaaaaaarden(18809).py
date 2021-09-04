import sys
import itertools as t
i = sys.stdin.readline
l, a = lambda: map(int, i().split()), range
n, m, g, r = l()
b, h, z = [[*l()] for _ in a(n)], r+g, 0
s = [(i*m+j) for i in a(n) for j in a(m) if b[i][j] == 2]
p = set(t.permutations(('g'*g)+('r'*r), h))
c = [*t.combinations(s, h)]

for w in c:
    for q in p:
        u = [(v//m, v % m) for v in w]
        o = 0
        l = [0] * (n*m)
        for i in a(h):
            y, x = u[i]
            b[y][x] = (q[i], 0)
        for y, x in u:
            if not l[(y*m+x)]:
                i, j = b[y][x]
                for d, e in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if 0 <= d < m and 0 <= e < n and b[e][d] and not l[(e*m+d)]:
                        g = b[e][d]
                        if g == 1 or g == 2:
                            u += [(e, d)]
                            b[e][d] = (i, j+1)
                            continue
                        f, k = g
                        if i != f and j+1 == k:
                            l[(e*m+d)] = 1
                            o += 1
        z = max(z, o)
        for y, x in u:
            b[y][x] = 1

print(z)
