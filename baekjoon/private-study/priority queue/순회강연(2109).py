import heapq as H
Q = []
for d, p in sorted((*map(int, input().split()[::-1]),)for _ in ' '*int(input())):
    H.heappush(Q, p)
    d < len(Q) and H.heappop(Q)
print(sum(Q))
