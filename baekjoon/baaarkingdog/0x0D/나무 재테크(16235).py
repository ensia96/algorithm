import sys
import collections as c
l, r = lambda: map(int, sys.stdin.readline().split()), range
n, m, k = l()
i, g = [[*l()]for _ in r(n)], [[5]*n for _ in r(n)]
t = {(p, q): c.deque()for p in r(n) for q in r(n)}
for z, y, x in sorted([[*l()][::-1] for _ in r(m)]):
    t[(y-1, x-1)].append(z)
while k:
    for y, x in t:
        dt, u = 0, len(t[(y, x)])
        while u:
            a, u = t[(y, x)].popleft(), u-1
            if g[y][x] >= a:
                g[y][x] -= a
                t[(y, x)].append(a+1)
            else:
                dt += a//2
        g[y][x] += dt
    for y, x in [*t]:
        for a in t[(y, x)]:
            if not a % 5:
                for p, q in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    if 0 <= y+p < n and 0 <= x+q < n:
                        t[(y+p, x+q)].appendleft(1)
    for y in r(n):
        for x in r(n):
            g[y][x] += i[y][x]
    k -= 1
print(sum(map(lambda x: len(t[x]), t)))
