import sys
import heapq as h
I = sys.stdin.readline
n, H = int(I()), []
for _ in ' '*n:
    for i in map(int, I().split()):
        h.heappush(H, i)
        if len(H) > n:
            h.heappop(H)
print(H[0])
