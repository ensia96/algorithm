import heapq as h
import sys
I, i, d = sys.stdin.readline, h.heappush, h.heappop
h, A = [], 0
for _ in ' '*int(I()):
    i(h, int(I()))
while len(h) > 1:
    a = d(h)+d(h)
    A += a
    i(h, a)
print(A)
