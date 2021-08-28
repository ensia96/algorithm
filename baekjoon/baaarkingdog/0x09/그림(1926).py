import sys
import collections as c

i, r, p = lambda: map(int, sys.stdin.readline().split()), range, print
l, w = i()
v, b = [[0] * l for _ in range(l)], [[*i()] for _ in range(l)]
q, d, t = c.deque([]), [(1, 0), (0, 1), (-1, 0), (0, -1)], []


for i in r(l):
    for j in r(w):
        if b[i][j]:
            b[i][j], c = 0, 1
            q.append((i, j))
            while q:
                u, v = q.popleft()
                for x, y in d:
                    n = u + y
                    m = v + x
                    if 0 <= n < l and 0 <= m < w and b[n][m]:
                        b[n][m] = 0
                        c += 1
                        q.append((n, m))
            t.append(c)

p(len(t))
p(max(t) if t else 0)
