import heapq as h
H = []
for _ in ' '*int(input()):
    x = int(input())
    if x:
        h.heappush(H, -x)
    else:
        print(-h.heappop(H or [0]))
