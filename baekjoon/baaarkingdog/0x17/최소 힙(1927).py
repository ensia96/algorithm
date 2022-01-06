import sys
import heapq as h
I = sys.stdin.readline
H = []
for _ in ' '*int(I()):
    x = int(I())
    if x:
        h.heappush(H, x)
    else:
        print(h.heappop(H or [0]))
