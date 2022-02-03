import heapq as h
n = int(input())
C = [0]+[(0, *map(int, input().split()))for _ in ' '*n]
V, Q = [1]+[0]*n, [(0, 1)]
A = E = 0
while Q:
    w, i = h.heappop(Q)
    if V[i]:
        continue
    V[i], A, E = 1, A+w, E+1
    if E == n:
        break
    for j in range(1, n+1):
        if C[i][j]:
            h.heappush(Q, (C[i][j], j))
print(A)
