import sys
import heapq as h
I, i, d = sys.stdin.readline, h.heappush, h.heappop
h = []
for _ in ' '*int(I()):
    a = int(I())
    if a:
        i(h, (abs(a), (a > 0)))
    else:
        a, f = d(h or [[0, 0]])
        print(a*(f-(not f)))
