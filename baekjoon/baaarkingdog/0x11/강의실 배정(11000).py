import sys
import heapq as h

I = sys.stdin.readline
l = [0]
i = h.heappush
p = h.heappop

for s, e in sorted((*map(int, I().split()),)for _ in ' '*int(I())):
    s < l[0] or p(l)
    i(l, e)
print(len(l))
