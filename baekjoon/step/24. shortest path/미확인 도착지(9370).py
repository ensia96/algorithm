import heapq as P
l, M = lambda: map(int, input().split()), 8**8


def f(x):
    Q, D = [(0, x)], [M]*-~n
    D[x] = 0
    while Q:
        x, y = P.heappop(Q)
        if D[y]-x:
            continue
        for i, j in E[y]:
            if D[j] > D[y]+i:
                D[j] = D[y]+i
                P.heappush(Q, (D[j], j))
    return D


for _ in ' '*next(l()):
    n, m, t = l()
    s, g, h = l()
    E = [[]for _ in ' '*-~n]
    for _ in ' '*m:
        a, b, d = l()
        E[a] += (d, b),
        E[b] += (d, a),
    T = [int(input())for _ in ' '*t]
    S, G, H = f(s), f(g), f(h)
    print(*sorted(t for t in T if S[t] in [S[g]+G[h]+H[t], S[h]+H[g]+G[t]]))
