import heapq as h
i, d = h.heappush, h.heappop


def D(L, f):
    while L and L[0]*f not in E:
        d(L)
    if E:
        t = d(L)*f
        if E[t]:
            E[t] -= 1
        else:
            E.pop(t)


for _ in ' '*int(input()):
    E, Q, q = {}, [], []
    for _ in ' '*int(input()):
        o, n = input().split()
        n = int(n)
        if o == 'I':
            E[n] = E.get(n, -1)+1
            i(Q, -n), i(q, n)
        else:
            D(Q, -1) if n > 0 else D(q, 1)
    print(f"{max(E)} {min(E)}"if E else'EMPTY')
