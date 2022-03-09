import sys
import heapq as h
L, M = lambda: map(int, sys.stdin.readline().split()), 2**34
n, m, k = L()
n += 1
D, E, Q = [M]*n, [[]for _ in ' '*n], []
for _ in ' '*m:
    u, v, c = L()
    E[v] += (c, u),
for i in L():
    h.heappush(Q, (0, i))
    D[i] = 0
while Q:
    x, y = h.heappop(Q)
    if D[y]-x:
        continue
    for i, j in E[y]:
        if D[j] > D[y]+i:
            D[j] = D[y]+i
            h.heappush(Q, (D[j], j))
a = 1
for i in range(2, n):
    if D[i] > D[a]:
        a = i
print(a)
print(D[a])
