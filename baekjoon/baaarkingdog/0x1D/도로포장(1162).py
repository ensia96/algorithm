import heapq as h
L, M = lambda: map(int, input().split()), 10**10
n, m, k = L()
n += 1
E = [[]for _ in ' '*n]
for _ in ' '*m:
    u, v, d = L()
    E[u] += (d, v),
    E[v] += (d, u),
D, Q = [[M]*-~k for _ in ' '*n], [(0, 0, 1)]
D[1][0] = 0
while Q:
    x, y, z = h.heappop(Q)
    t = D[z][x]
    if t-y:
        continue
    for i, j in E[z]:
        if D[j][x] > t+i:
            D[j][x] = t+i
            h.heappush(Q, (x, D[j][x], j))
        if x < k and D[j][x+1] > t:
            D[j][x+1] = t
            h.heappush(Q, (x+1, D[j][x+1], j))
print(min(D[n-1]))
