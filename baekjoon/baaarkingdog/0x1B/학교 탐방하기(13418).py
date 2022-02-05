import heapq as h
n, m = map(int, input().split())
n += 1
E = [[] for _ in ' '*n]
for _ in ' '*-~m:
    i, j, w = map(int, input().split())
    E[i] += (not w, j),
    E[j] += (not w, i),


def F(x):
    a = e = 0
    V, Q = [0]*n, [(0, 0)]
    while Q:
        w, i = h.heappop(Q)
        if V[i]:
            continue
        V[i], a, e = 1, a+w, e+1
        if e == n:
            return a**2
        for w, j in E[i]:
            h.heappush(Q, (w*x, j))


print(F(-1)-F(1))
