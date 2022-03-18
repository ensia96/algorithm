import sys
import heapq as h
L, M = lambda: map(int, input().split()), 20**9
n, m, k = L()
n += 1
E = [[]for _ in ' '*n]
for _ in ' '*m:
    a, b, c = L()
    E[a] += (c, b),
D, Q = [[-M]*k for _ in ' '*n], [(0, 1)]
while Q:
    x, y = h.heappop(Q)
    for i, j in E[y]:
        if D[j][0] < -x-i:
            h.heappush(D[j], -x-i)
            h.heappop(D[j])
            h.heappush(Q, (x+i, j))
for d in D[1:]:
    print(-1 if -d[0] == M else -d[0])
