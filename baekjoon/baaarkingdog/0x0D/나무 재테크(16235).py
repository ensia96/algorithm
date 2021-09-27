import sys
from collections import deque
l, r = lambda: map(int, sys.stdin.readline().split()), range
n, m, k = l()
i, g, t = [[*l()]for _ in r(n)], [5]*n*n, [deque()for _ in r(n*n)]
for x, y, z in sorted([[*l()]for _ in r(m)]):
    t[(x-1)*n+y-1].append(z)
for _ in r(k):
    for p in r(n*n):
        dt, u = 0, len(t[p])
        while u:
            a, u = t[p].popleft(), u-1
            if g[p] < a:
                dt += a//2
            else:
                g[p] -= a
                t[p].append(a+1)
        g[p] += dt
    for z in r(n*n):
        for a in t[z]:
            if not a % 5:
                for p, q in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    if 0 <= z//n+p < n and 0 <= z % n+q < n:
                        t[(z//n+p)*n+z % n+q].appendleft(1)
    for p in r(n*n):
        g[p] += i[p//n][p % n]
print(sum(len(t[p])for p in r(n*n)))
