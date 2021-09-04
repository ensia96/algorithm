from collections import deque as d
l, g = lambda: map(int, input().split()), range
n, m = l()
b, v, w, u = [[*l()] for _ in g(n)], [], 3, 64

for i in g(n):
    for j in g(m):
        if b[i][j] == 2:
            v += [(i, j)]
        elif b[i][j] == 1:
            w += 1


def e(c):
    global u
    if c == 3:
        q, a, t = d(v), [[0]*m for _ in g(n)], 0
        while q:
            i, j = q.popleft()
            for y, x in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= y < n and 0 <= x < m and not a[y][x] and not b[y][x]:
                    a[y][x], t = 1, t+1
                    q.append((y, x))
        u = min(u, t)
        return
    for i in g(n):
        for j in g(m):
            if not b[i][j]:
                b[i][j] = 1
                e(c+1)
                b[i][j] = 0


e(0)
print(m*n-len(v)-w-u)
