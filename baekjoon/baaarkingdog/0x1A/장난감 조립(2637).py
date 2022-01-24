import heapq as h
n = int(input())+1
C, D, A, Q = [[]for _ in ' '*n], [0]*n, [0]*~-n+[1], [n-1]
for _ in ' '*int(input()):
    x, y, k = map(int, input().split())
    C[x] += (y, k),
    D[y] += 1
while Q:
    p = h.heappop(Q)
    for c, w in C[p]:
        D[c] -= 1
        A[c] += A[p]*w
        if not D[c]:
            h.heappush(Q, c)
for i in range(1, n-1):
    if not C[i]:
        print(i, A[i])
