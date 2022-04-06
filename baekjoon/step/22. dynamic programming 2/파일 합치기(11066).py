import heapq as h
d = h.heappop
for _ in ' '*int(input()):
    k, t = int(input()), 0
    F = [*map(int, input().split())]
    h.heapify(F)
    for _ in ' '*~-k:
        x, y = d(F), d(F)
        h.heappush(F, x+y)
        t += x+y
    print(t)
