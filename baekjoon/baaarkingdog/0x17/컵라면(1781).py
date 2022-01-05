import sys
import heapq as h
I, i, d = sys.stdin.readline, h.heappush, h.heappop
n, p, a = int(I()), [], []
for _ in ' '*n:
    x, y = map(int, I().split())
    i(p, (x, -y))
while p and len(a) < n:
    x, y = d(p)
    if x > len(a):
        i(a, -y)
    elif a[0] < -y:
        d(a) and i(a, -y)
print(sum(a))
