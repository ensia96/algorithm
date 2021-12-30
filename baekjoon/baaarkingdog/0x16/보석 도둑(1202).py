import sys
import heapq as h
I, i, d = sys.stdin.readline, h.heappush, h.heappop
a, J, C, l = 0, [], [], lambda: map(int, I().split())
n, k = l()
for _ in ' '*n:
    m, v = l()
    i(J, (m, -v))
for _ in ' '*k:
    i(C, int(I()))
while J and C:
    m, v = d(J)
    c = d(C)
    while C and c < m:
        c = d(C)
    if c >= m:
        a += -v
print(a)
