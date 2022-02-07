import sys
import heapq as h
I = sys.stdin.readline
l, A = lambda: map(int, input().split()), 0
n, m, k = l()
C, G = [[]for _ in ' '*-~n], [*l()]
g = len(G)
for i in range(g):
    for j in range(i+1, g):
        C[G[i]] += (0, G[j]),
for _ in ' '*m:
    i, j, w = l()
    C[i] += (w, j),
    C[j] += (w, i),
Q, V, E = [(0, 1)], [0]*-~n, 0
while Q:
    w, i = h.heappop(Q)
    if V[i]:
        continue
    V[i], A, E = 1, A+w, E+1
    if E == n:
        break
    for D in C[i]:
        h.heappush(Q, D)
print(A)
