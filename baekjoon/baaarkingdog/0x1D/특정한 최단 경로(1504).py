import heapq as h
L, M = lambda: map(int, input().split()), 8**8
n, e = L()
n += 1
E = [[]for _ in ' '*n]
for _ in ' '*e:
    a, b, c = L()
    E[a] += (c, b),
    E[b] += (c, a),
u, v = L()


def F(s):
    D, Q = [M]*n, [(0, s)]
    D[s] = 0
    while Q:
        x, y = h.heappop(Q)
        if D[y]-x:
            continue
        for i, j in E[y]:
            if D[j] > D[y]+i:
                D[j] = D[y]+i
                h.heappush(Q, (D[j], j))
    return D


A, B = F(1), F(n-1)
t = F(u)[v]+min(A[u]+B[v], A[v], B[u])
print(-1 if t > M else t)
