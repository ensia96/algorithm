import sys
import heapq as h
L, M = lambda: map(int, sys.stdin.readline().split()), 8**8
n, m, k = L()
s, d = L()
n += 1
E = [[]for _ in ' '*n]
for _ in ' '*m:
    a, b, w = L()
    E[a] += (w, b),
    E[b] += (w, a),
D, Q = [[M]*n for _ in ' '*n], [(0, s, 0)]
D[s][0] = 0
while Q:
    x, y, z = h.heappop(Q)
    if min(D[y][:z+1]) < x or z > n-2 or y == d:
        continue
    for i, j in E[y]:
        if D[j][z+1] > D[y][z]+i:
            D[j][z+1] = D[y][z]+i
            h.heappush(Q, (D[j][z+1], j, z+1))
print(min(D[d]))
for _ in ' '*k:
    a = next(L())
    for i in range(n):
        if D[d][i] != M:
            D[d][i] += a*i
    print(min(D[d]))
