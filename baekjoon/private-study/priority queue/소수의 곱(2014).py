import heapq as H
k, n = map(int, input().split())
A = [*map(int, input().split())]
Q = [(A[i], i)for i in range(k)]
s = set()
f = 1
while f:
    x, y = H.heappop(Q)
    s.add(x)
    for i in range(y, k):
        x*A[i] in s or H.heappush(Q, (x*A[i], i))
        n > len(s) or exit(print(sorted([*s])[n-1]))
