import sys
import collections as c

i, r, p = sys.stdin.readline, range, lambda: map(int, i().split())
m, n, k = p()
b, d = [[0] * n for _ in r(m)], [(1, 0), (0, 1), (-1, 0), (0, -1)]
a, o, q = 0, [], c.deque()

for _ in r(k):
    e, f, g, h = p()
    for u in r(f, h):
        for v in r(e, g):
            b[u][v] = 1


for w in r(m):
    for z in r(n):
        if not b[w][z]:
            a += 1
            c = 1
            b[w][z] = 1
            q.append((w, z))
            while q:
                s, t = q.popleft()
                for x, y in d:
                    j, l = s + y, t + x
                    if 0 <= j < m and 0 <= l < n and not b[j][l]:
                        c += 1
                        b[j][l] = 1
                        q.append((j, l))
            o.append(c)

print(a)
print(*sorted(o))
