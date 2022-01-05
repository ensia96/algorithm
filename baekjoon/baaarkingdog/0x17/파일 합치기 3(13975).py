import sys
import heapq as h
I, i, d = sys.stdin.readline, h.heappush, h.heappop
for _ in ' '*int(I()):
    _, A, F = int(I()), 0, []
    for f in map(int, I().split()):
        i(F, f)
    while len(F) > 1:
        f = d(F)+d(F)
        i(F, f)
        A += f
    print(A)
