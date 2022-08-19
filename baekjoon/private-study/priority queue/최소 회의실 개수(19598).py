import heapq as H
n = int(input())
A = sorted((*map(int, input().split()),)for _ in ' '*n)
Q = []
R = 0
for s, e in A:
    H.heappush(Q, e)
    while Q and Q[0] <= s:
        H.heappop(Q)
    R = max(R, len(Q))
print(R)
