import heapq as H
n = int(input())
Q = []
for _ in ' '*n:
    a, *A = map(int, input().split())
    if a:
        for a in A:
            H.heappush(Q, -a)
    else:
        print(-H.heappop(Q)if Q else -1)
