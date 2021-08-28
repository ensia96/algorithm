import sys
import collections as c

i = sys.stdin.readline
j, f, d = c.deque(), c.deque(), [(1, 0), (0, 1), (-1, 0), (0, -1)]

r, c = map(int, i().split())
b, a = [[*i().strip()] for _ in range(r)], 1

for n in range(r):
    for m in range(c):
        if b[n][m] == 'J':
            b[n][m] = 1
            j.append((n, m))
        if b[n][m] == 'F':
            f.append((n, m))
        if b[n][m] == '#':
            b[n][m] = 0

while j and f:
    n, m = j.popleft()
    v, w = f.popleft()
    for x, y in d:
        p, q = n + y, m + x
        g, h = v + y, w + x
        if 0 <= g < r and 0 <= h < c and b[g][h]:
            b[g][h] = 'F'
            f.append((g, h))
        if 0 <= p < r and 0 <= q < c and b[p][q] == '.':
            a += 1
            j.append((p, q))

print(a if any('.' in l for l in b) else 'IMPOSSIBLE')
