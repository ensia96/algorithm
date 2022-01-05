import sys
import heapq as h
I, i, d, l, r = sys.stdin.readline, h.heappush, h.heappop, [], []
for c in range(int(I())):
    x, m = int(I()), (c+1)//2
    if (r or [-10001])[0] < x:
        i(r, x)
        if m > len(l):
            i(l, -d(r))
    else:
        i(l, -x)
        if m < len(l):
            i(r, -d(l))
    print(-l[0]if len(l) == len(r)else r[0])
