import heapq as h
import collections as c
i, d = h.heappush, h.heappop


def D(L, f):
    while L and not E[L[0]*(f and -1 or 1)]:
        d(L)
    if L:
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
            D(Q, 1) if n > 0 else D(q, 0)
    print(Q and q and f"{d(Q)} {d(q)}" or 'EMPTY')
