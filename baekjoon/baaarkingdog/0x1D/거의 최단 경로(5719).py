import heapq as h
L, M = lambda: map(int, input().split()), 8**8
while 1:
    n, m = L()
    if not n:
        break
    s, d = L()
    E, t = [{}for _ in ' '*n], 0
    for _ in ' '*m:
        u, v, p = L()
        E[u][v] = p
    while 1:
        R, D, Q = [s]*n, [M]*n, [(0, s)]
        D[s] = 0
        while Q:
            x, y = h.heappop(Q)
            if D[y]-x:
                continue
            for i in E[y]:
                if D[i] > D[y]+E[y][i]:
                    D[i], R[i] = D[y]+E[y][i], y
                    h.heappush(Q, (D[i], i))
        if D[d] == M or t and t < D[d]:
            break
        r, t = [d], D[d]
        while r[-1]-s:
            r += R[r[-1]],
            E[r[-1]].pop(r[-2])
    print(-(not D[d]-M) or D[d])
