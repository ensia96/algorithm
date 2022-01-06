import heapq as h
n, H = int(input()), []
for _ in range(n):
    for i in map(int, input().split()):
        h.heappush(H, i)
        if len(H) > n:
            h.heappop(H)
print(H[0])
