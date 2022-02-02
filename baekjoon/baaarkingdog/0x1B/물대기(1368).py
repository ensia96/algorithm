import heapq as h
n = int(input())
G = [int(input())for _ in ' '*n]
G = [(0, *G)]+[(G[i], *map(int, input().split()))for i in range(n)]
V, Q = [0]*(n+1), [(0, 1)]
E = A = 0
while Q:
    w, i = h.heappop(Q)
    if V[i]:
        continue
    V[i], A, E = 1, A+w, E+1
    if E == n-1:
        break
    for j in range(n+1):
        h.heappush(Q, (G[i][j], j))
print(A)
