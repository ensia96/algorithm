import heapq as H
n = int(input())
A = sorted((sorted(map(int, input().split()))
           for _ in ' '*n), key=lambda x: x[::-1])
d = int(input())
Q, R = [], 0
for x, y in A:
    if y <= x+d:
        H.heappush(Q, x)
        while Q:
            if y-Q[0] <= d:
                break
            H.heappop(Q)
        R = max(R, len(Q))
print(R)
