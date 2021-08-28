import collections as c

i, r = input, range
n, m = map(int, i().split())
q, d = c.deque([(0, 0, 1)]), [(1, 0), (0, 1), (-1, 0), (0, -1)]
v, b = [[1] * m for _ in r(n)], [[*map(int, [*i()])] for _ in r(n)]

while q:
    u, w, l = q.popleft()
    v[u][w] = 0
    b[u][w] = l
    for x, y in d:
        g, h = u + x, w + y
        if 0 <= g < n and 0 <= h < m and b[g][h] and v[g][h]:
            q.append((g, h, l + 1))

print(b[n - 1][m - 1])
