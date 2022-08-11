from heapq import*
Q = []
for d, w in sorted((*map(int, input().split()),)for _ in ' '*int(input())):
    heappush(Q, w)
    d < len(Q) and heappop(Q)
print(sum(Q))
