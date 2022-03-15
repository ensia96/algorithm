import sys
import heapq as h
L, M = lambda: map(int, sys.stdin.readline().split()), 10**15
n, m, a, b, c = L()
n += 1
E = [[]for _ in ' '*n]
A, l, r = -1, 0, 0
for _ in ' '*m:
    u, v, d = L()
    E[u] += (d, v),
    E[v] += (d, u),
    r = max(r, d)


def F(X):
    D, Q = [M]*n, [(0, a)]
    D[a] = 0
    while Q:
        x, y = h.heappop(Q)
        if D[y]-x:
            continue
        for i, j in E[y]:
            if (i <= X)*(D[j] > D[y]+i):
                D[j] = D[y]+i
                h.heappush(Q, (D[j], j))
    return D[b] <= c


while l <= r:
    m = (l+r)//2
    if F(m):
        r, A = m-1, m
    else:
        l = m+1
print(A)
