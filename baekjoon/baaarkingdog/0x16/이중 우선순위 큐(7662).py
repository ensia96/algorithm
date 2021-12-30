import heapq as h
import collections as c
i, d = h.heappush, h.heappop


def D(L, f, a):
    while L and not E[L[0]*(f and -1 or 1)]:
        d(L)
    if a and L:
        E[L[0]*(f and -1 or 1)] -= 1
        d(L)


for _ in ' '*int(input()):
    E, Q, q, k = c.defaultdict(int), [], [], int(input())
    for _ in ' '*k:
        o, n = input().split()
        n = int(n)
        if o == 'I':
            E[n] += 1
            i(Q, -n), i(q, n)
        elif Q:
            D(Q, 1, 1) if n > 0 else D(q, 0, 1)
    D(Q, 1, 0), D(q, 0, 0)
    print(Q and q and f"{-Q[0]} {q[0]}" or 'EMPTY')
