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
D, Q = [[M]*n for _ in ' '*n], [(0, 0, s)]
D[s][0] = 0
while Q:
    x, y, z = h.heappop(Q)
    if y > n-2:
        continue
    for i, j in E[z]:
        if D[j][y+1] > D[z][y]+i:
            D[j][y+1] = D[z][y]+i
            h.heappush(Q, (D[j][y+1], y+1, j))
print(min(D[d]))
for _ in ' '*k:
    a = next(L())
    for i in range(n):
        if D[d][i] != M:
            D[d][i] += a*i
    print(min(D[d]))
