import sys
import itertools as t
i = sys.stdin.readline
l, a = lambda: map(int, i().split()), range
n, m, g, r = l()
b, h, z = [[*l()] for _ in a(n)], r+g, 0
p = set(t.permutations(('g'*g)+('r'*r), h))
c = [*t.combinations([(i*m+j) for i in a(n) for j in a(m) if b[i][j] == 2], h)]

for w in c:
    for q in p:
        u, o, l = [(v//m, v % m) for v in w], 0, [1] * (n*m)
        for i in a(h):
            y, x = u[i]
            b[y][x] = (q[i], 0)
        for y, x in u:
            if l[(y*m+x)]:
                i, j = b[y][x]
                for d, e in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                    if 0 <= d < m and 0 <= e < n and b[e][d] and l[(e*m+d)]:
                        g = b[e][d]
                        if g in [1, 2]:
                            u += [(e, d)]
                            b[e][d] = (i, j+1)
                        else:
                            if i != g[0] and j+1 == g[1]:
                                l[(e*m+d)] = 0
                                o += 1
        z = max(z, o)
        for y, x in u:
            b[y][x] = 1

print(z)
