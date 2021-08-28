import sys
import collections as c

i, r, d = sys.stdin.readline, range, [(1, 0), (0, 1), (-1, 0), (0, -1)]

for _ in r(int(i().strip())):
    m, n, k = map(int, i().split())
    a, b, q = 0, [[0] * m for _ in r(n)], c.deque()

    for __ in range(k):
        x, y = map(int, i().split())
        b[y][x] = 1

    for f in r(n):
        for j in r(m):
            if b[f][j]:
                a += 1
                q.append((f, j))
                while q:
                    g, h = q.popleft()
                    b[g][h] = 0
                    for x, y in d:
                        v, w = g + y, h + x
                        if 0 <= v < n and 0 <= w < m and b[v][w]:
                            b[v][w] = 0
                            q.append((v, w))
    print(a)
