import collections as c

i = input
n, m = map(int, i().split())
q, d = c.deque([(0, 0)]), [(1, 0), (0, 1), (-1, 0), (0, -1)]
b = [[*map(int, [*i()])] for _ in range(n)]

while q:
    u, w = q.popleft()
    for x, y in d:
        g, h = u + x, w + y
        if 0 <= g < n and 0 <= h < m and b[g][h] == 1:
            b[g][h] = b[u][w] + 1
            q.append((g, h))

print(b[n - 1][m - 1])
