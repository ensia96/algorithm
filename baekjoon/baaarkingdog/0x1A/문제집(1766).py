import sys
import heapq as h
I, p = sys.stdin.readline, h.heappush
n, m = map(int, I().split())
n += 1
A, C, D, Q = [], [[]for _ in ' '*n], [0]*n, []
for _ in ' '*m:
    a, b = map(int, I().split())
    C[a] += b,
    D[b] += 1
for x in range(1, n):
    p(Q, (D[x], x))
while Q:
    a, b = h.heappop(Q)
    if a:
        continue
    A += b,
    for c in C[b]:
        D[c] -= 1
        p(Q, (D[c], c))
print(*A)
