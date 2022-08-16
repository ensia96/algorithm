import heapq as H
n = int(input())
A = sorted(sorted(map(int, input().split()))[::-1]for _ in ' '*n)
d = int(input())
Q, R = [], 0
for y, x in A:
    H.heappush(Q, x)
    Q and y-d > Q[0] and H.heappop(Q)
    R = max(R, len(Q))
print(R)
