import heapq as h
L, M = lambda: map(int, input().split()), 8**8


def F():
    Q, D[s] = [(0, s)], 0
    while Q:
        x, y = h.heappop(Q)
        if D[y]-x:
            continue
        for i in E[y]:
            t = D[y]+E[y][i]
            if D[i] > t:
                D[i] = t
                h.heappush(Q, (t, i))


def X():
    Q = [d]
    for a in Q:
        if a == s:
            continue
        for b in R[a]:
            if E[b].get(a) and not D[b]+E[b][a]-D[a]:
                del E[b][a]
                Q += b,


while 1:
    n, m = L()
    if not n:
        break
    s, d = L()
    E, R = [{}for _ in ' '*n], [{}for _ in ' '*n]
    for _ in ' '*m:
        u, v, p = L()
        E[u][v] = R[v][u] = p
    D = [M]*n
    F()
    X()
    D = [M]*n
    F()
    print(-(D[d] == M) or D[d])
