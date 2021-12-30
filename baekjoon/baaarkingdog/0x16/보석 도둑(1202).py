import sys
import heapq as h
I, i, d = sys.stdin.readline, h.heappush, h.heappop
a, J, l = 0, [], lambda: map(int, I().split())
n, k = l()
for _ in ' '*n:
    m, v = l()
    i(J, (-v, m))
for c in sorted(int(I())for _ in ' '*k):
    T = []
    while J:
        v, m = d(J)
        if m <= c:
            a += -v
            break
        else:
            i(T, (v, m))
    J = [*h.merge(J, T)]
print(a)
