import heapq as h
l, i, p = lambda: map(int, input().split()), h.heappush, h.heappop
n, m = l()
a = sorted(l())
for _ in range(m):
    s = p(a)+p(a)
    i(a, s)+i(a, s)
print(sum(a))
