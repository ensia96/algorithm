import sys
import heapq as h
L, M = lambda: map(int, sys.stdin.readline().split()), 10**16
n, m = L()
n += 1
E = [[]for _ in ' '*n]
for i in range(m):
    a, b = L()
    E[a] += (i, b),
    E[b] += (i, a),
D, Q = [M]*n, [(0, 1)]
D[1] = 0
while Q:
    x, y = h.heappop(Q)
    if D[y]-x:
        continue
    for i, j in E[y]:
        t = i+m*(x//m)
        while t <= x:
            t += m
        if D[j] > t:
            D[j] = t
            h.heappush(Q, (t, j))
print(D[n-1])
