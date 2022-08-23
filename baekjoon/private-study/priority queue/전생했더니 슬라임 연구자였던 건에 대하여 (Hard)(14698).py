import sys
import heapq as H
M = 1000000007
I = sys.stdin.readline
for _ in ' '*int(I()):
    n, Q, A = int(I()), [*map(int, I().split())], 1
    H.heapify(Q)
    while len(Q) > 1:
        x = H.heappop(Q)*H.heappop(Q)
        H.heappush(Q, x)
        A = A*x % M
    print(A)
