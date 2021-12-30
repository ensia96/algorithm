import sys
import heapq as h
I, L, T = sys.stdin.readline, lambda: map(int, I().split()), []
n, k = L()
J = sorted((*L(),)for _ in ' '*n)
a = j = 0
for c in sorted(int(I())for _ in ' '*k):
    while j < n and c >= J[j][0]:
        h.heappush(T, -J[j][1])
        j += 1
    if T:
        a += -h.heappop(T)
print(a)
