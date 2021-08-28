import sys
import collections as c

i, r = lambda: map(int, sys.stdin.readline().split()), range


l, w = i()
v, b = [[0] * l for _ in range(l)], [[*i()] for _ in range(l)]
q, d, t = c.deque([]), [(1, 0), (0, 1), (-1, 0), (0, -1)], []


def f(i, j, c=1):
    for x, y in d:
        n, m = i + y, j + x
        if 0 <= n < l and 0 <= m < w and b[n][m]:
            b[n][m] = 0
            c += 1
            q.append((n, m))
    return f(*q.popleft(), c) if q else c


for i in r(l):
    for j in r(w):
        if b[i][j]:
            b[i][j] = 0
            t.append(f(i, j))

print(len(t))
print(max(t))
