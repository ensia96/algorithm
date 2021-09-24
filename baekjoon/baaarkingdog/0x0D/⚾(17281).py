import itertools as t
import sys
i, g = sys.stdin.readline, range
n = [[*map(int, i().split())]for _ in g(int(i()))]
a, u = 0, [*t.permutations(g(1, 9))]
for m in u:
    i, p, e = 0, 0, m[:3]+(0,)+m[3:]
    for t in n:
        x = y = z = o = 0
        while o < 3:
            if not t[e[i]]:
                o += 1
            elif t[e[i]] == 1:
                p, x, y, z = p+z, 1, x, y
            elif t[e[i]] == 2:
                p, x, y, z = p+y+z, 0, 1, x
            elif t[e[i]] == 3:
                p, x, y, z = p+x+y+z, 0, 0, 1
            else:
                p, x, y, z = p+x+y+z+1, 0, 0, 0
            i = (i+1) % 9
    a = max(a, p)
print(a)
