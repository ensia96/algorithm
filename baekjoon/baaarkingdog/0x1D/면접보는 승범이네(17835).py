import sys
import heapq as h
L, M = lambda: map(int, sys.stdin.readline().split()), 2**34
n, m, k = L()
n += 1
t = [L()for _ in ' '*m]
T = {i: n for i in L()}
E = [[]for _ in ' '*-~n]
for u, v, c in t:
    E[T.get(v, v)] += (c, u),
D, Q = [M]*-~n, [(0, n)]
D[n] = 0
while Q:
    x, y = h.heappop(Q)
    if D[y]-x or T.get(y):
        continue
    for i, j in E[y]:
        if D[j] > D[y]+i:
            D[j] = D[y]+i
            h.heappush(Q, (D[j], j))
a = n
for i in range(1, n+1):
    if not T.get(i) and D[i] > D[a]:
        a = i
print(a)
print(D[a])
