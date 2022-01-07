import sys
import heapq as h
I, H = sys.stdin.readline, []
for _ in ' '*int(I()):
    x = int(I())
    if x:
        h.heappush(H, -x)
    else:
        print(-h.heappop(H or [0]))
