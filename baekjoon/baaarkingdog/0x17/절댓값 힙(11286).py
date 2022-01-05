import sys
import heapq as h
I, i, d = sys.stdin.readline, h.heappush, h.heappop
h = []
for _ in ' '*int(I()):
    a = int(I())
    if a:
        i(h, (abs(a), a))
    else:
        print(len(h) and d(h)[1])
