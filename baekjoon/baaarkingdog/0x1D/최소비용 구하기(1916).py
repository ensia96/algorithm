import heapq as h
L, M = lambda: map(int, input().split()), 8**9
n = next(L())
m = next(L())
E = [[]for _ in ' '*n]
for _ in ' '*m:
    s, e, d = L()
    E[s-1] += (d, e-1),
u, v = L()
D = [M]*n
Q, D[u-1] = [(0, u-1)], 0
while Q:
    x, y = h.heappop(Q)
    if D[y]-x:
        continue
    for i, j in E[y]:
        if D[j] > D[y]+i:
            D[j] = D[y]+i
            h.heappush(Q, (D[j], j))
print(D[v-1])
