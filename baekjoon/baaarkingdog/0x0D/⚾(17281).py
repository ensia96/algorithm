import collections as l
import itertools as t
import sys
i, g = sys.stdin.readline, range
n = [[*map(int, i().split())]for _ in g(int(i()))]
a, u = 0, [*t.permutations(g(1, 9))]
for m in u:
    i, p, e = 0, 0, m[:3]+(0,)+m[3:]
    for t in n:
        b, o = l.deque([0]*3), 0
        while o < 3:
            c = t[e[i]]
            if c:
                p, c = p+b.popleft(), c-1
                b.append(1)
                while c:
                    p, c = p+b.popleft(), c-1
                    b.append(0)
            else:
                o += 1
            i = (i+1) % 9
    a = max(a, p)
print(a)
