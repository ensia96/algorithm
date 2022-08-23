import heapq as H
M = 1000000007
for _ in ' '*int(input()):
    n, Q, A = int(input()), [*map(int, input().split())], 1
    H.heapify(Q)
    while len(Q) > 1:
        x = H.heappop(Q)*H.heappop(Q)
        H.heappush(Q, x)
        A = A*x % M
    print(A)
