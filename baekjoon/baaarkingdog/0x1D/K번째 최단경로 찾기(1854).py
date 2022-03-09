import heapq as h
L, M = lambda: map(int, input().split()), 20**9
n, m, k = L()
n += 1
E = [[]for _ in ' '*n]
for _ in ' '*m:
    a, b, c = L()
    E[a] += (c, b),
D, Q = [[] for _ in ' '*n], [(0, 1)]
while Q:
    x, y = h.heappop(Q)
    if not len(D[y])-k:
        continue
    D[y] += x,
    for i, j in E[y]:
        h.heappush(Q, (x+i, j))
for d in D[1:]:
    print(-1 if len(d)-k else d[k-1])
