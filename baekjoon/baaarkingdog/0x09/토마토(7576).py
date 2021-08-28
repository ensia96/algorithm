import sys
import collections as c

i, r = sys.stdin.readline, range
m, n = map(int, i().split())
b = [[*map(int, i().split())] for _ in r(n)]
q, d = c.deque([]), [(1, 0), (0, 1), (-1, 0), (0, -1)]


def f(l, c):
    for x, y in d:
        i, j = l + y, c + x
        if 0 <= i < n and 0 <= j < m and b[i][j] == 0:
            b[i][j] = b[l][c] + 1
            q.append((i, j))


for l in r(n):
    for c in r(m):
        if b[l][c] == 1:
            f(l, c)

while q:
    f(*q.popleft())

print(max([*map(max, b)]) - 1 if all(map(all, b)) else -1)
