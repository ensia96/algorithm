import heapq as h
M = 8**9
m, n = map(int, input().split())
B = [[*map(int, input())]for _ in ' '*n]
D = [[M]*m for _ in ' '*n]
Q, D[0][0] = [(0, 0, 0)], 0
while Q:
    z, x, y = h.heappop(Q)
    if D[x][y]-z:
        continue
    for p, q in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
        if (0 <= p < n)*(0 <= q < m) and D[p][q] > z+B[p][q]:
            D[p][q] = z+B[p][q]
            h.heappush(Q, (D[p][q], p, q))
print(D[n-1][m-1])
