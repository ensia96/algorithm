import heapq as h
L, M = lambda: map(int, input().split()), 8**8
n, m, k = L()
n += 1
E, R = [[]for _ in ' '*n], [[]for _ in ' '*n]
for _ in ' '*m:
    s, e, t = L()
    E[s] += (t, e),
    R[e] += (t, s),


def F(t):
    D, Q = [M]*n, [(0, k)]
    D[k] = 0
    while Q:
        x, y = h.heappop(Q)
        if D[y]-x:
            continue
        for i, j in t[y]:
            if D[j] > D[y]+i:
                D[j] = D[y]+i
                h.heappush(Q, (D[j], j))
    return D


print(max(*map(sum, [*zip(F(E), F(R))][1:])))
