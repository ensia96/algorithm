import sys
import heapq
L, M = lambda: map(int, sys.stdin.readline().split()), 8**8
v, e = L()
s = next(L())
v += 1
D = [M]*v
D[s] = 0
E = [[]for _ in ' '*v]
for _ in ' '*e:
    a, b, c = L()
    E[a] += (c, b),
Q = [(D[s], s)]
while Q:
    x, y = heapq.heappop(Q)
    if D[y] != x:
        continue
    for i, j in E[y]:
        if D[j] > D[y]+i:
            D[j] = D[y]+i
            heapq.heappush(Q, (D[j], j))
for d in D[1:]:
    print(d if d-M else 'INF')
