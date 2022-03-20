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
D, Q = [{}for _ in ' '*n], [(0, 0, s)]
D[s][0] = 0
while Q:
    x, y, z = h.heappop(Q)
    if y > n:
        continue
    for i, j in E[z]:
        if D[j].get(y+1, M) > D[z][y]+i:
            D[j][y+1] = D[z][y]+i
            h.heappush(Q, (D[j][y+1], y+1, j))
print(min(D[d].values()))
for _ in ' '*k:
    a = next(L())
    for i in D[d]:
        D[d][i] += a*i
    print(min(D[d].values()))
