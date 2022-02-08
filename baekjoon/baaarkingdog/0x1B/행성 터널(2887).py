import sys
import heapq as h
I = sys.stdin.readline
n = int(I())
P = [(*map(int, I().split()), i)for i in range(n)]
G = [[]for _ in ' '*n]
for j in range(3):
    P.sort(key=lambda x: x[j])
    for i in range(1, n):
        w = abs(P[i][j]-P[i-1][j])
        G[P[i-1][3]] += (w, P[i][3]),
Q, V = [(0, 0)], [0]*n
A = E = 0
while Q:
    w, i = h.heappop(Q)
    if V[i]:
        continue
    V[i], A, E = 1, A+w, E+1
    if E == n:
        break
    for D in G[i]:
        h.heappush(Q, D)
print(A)
