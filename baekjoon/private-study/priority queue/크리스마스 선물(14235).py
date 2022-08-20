import heapq as H
n = int(input())
Q = []
for _ in ' '*n:
    a, *A = map(int, input().split())
    if a:
        Q += [-a for a in A]
        H.heapify(Q)
    else:
        print(-H.heappop(Q)if Q else -1)
