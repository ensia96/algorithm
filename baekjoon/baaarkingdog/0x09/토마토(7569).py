import sys
import collections as c

i, r = sys.stdin.readline, range
q, d = c.deque(), [(1, 0, 0), (-1, 0, 0), (0, 1, 0),
                   (0, -1, 0), (0, 0, 1), (0, 0, -1)]
m, n, h = map(int, i().split())

b, f = [[[*map(int, i().split())] for __ in r(n)] for _ in r(h)], 0


def a():
    m = 0
    for s in b:
        for l in s:
            if not all(l):
                return -1
            m = max(m, max(l))
    return m - 1


for z1 in r(h):
    for y1 in r(n):
        for x1 in r(m):
            if b[z1][y1][x1] == 1:
                q.append((z1, y1, x1))

while q:
    z1, y1, x1 = q.popleft()
    for z, y, x in d:
        z2, y2, x2 = z1 + z, y1 + y, x1 + x
        if 0 <= z2 < h and 0 <= y2 < n and 0 <= x2 < m and not b[z2][y2][x2]:
            b[z2][y2][x2] = b[z1][y1][x1] + 1
            q.append((z2, y2, x2))

print(a())
