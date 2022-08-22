import heapq as H
n, d = map(int, input().split())
A = [*map(int, input().split())]
a = A[0]
Q = [(-a, 0)]
for i in range(1, n):
    while Q and i+Q[0][1] > d:
        H.heappop(Q)
    x, y = H.heappop(Q)
    H.heappush(Q, (-max(A[i]-x, A[i]), -i))
    a = max(a, -Q[0][0])
    H.heappush(Q, (x, y))
print(a)
