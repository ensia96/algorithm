import heapq as h
L, M = lambda: map(int, input().split()), 8**8
n = next(L())+1
D, R, E = [M]*n, [M]*n, [[]for _ in ' '*n]
for _ in ' '*next(L()):
    s, e, d = L()
    E[s] += (d, e),
s, e = L()
D[s], Q = 0, [(0, s)]
while Q:
    x, y = h.heappop(Q)
    if D[y] != x:
        continue
    for i, j in E[y]:
        if D[j] > D[y]+i:
            D[j], R[j] = D[y]+i, y
            h.heappush(Q, (D[j], j))
r = [e]
while r[-1]-s:
    r += R[r[-1]],
print(D[e])
print(len(r))
print(*r[::-1])
