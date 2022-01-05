import heapq as h
i, d = h.heappush, h.heappop
h = []
for _ in ' '*int(input()):
    a = int(input())
    if a:
        i(h, (abs(a), (a > 0)))
    else:
        a, f = d(h or [[0, 0]])
        print(a*(f-(not f)))
