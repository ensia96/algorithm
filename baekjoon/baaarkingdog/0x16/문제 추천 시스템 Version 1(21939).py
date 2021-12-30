import sys
import heapq as h
I, i, d = sys.stdin.readline, h.heappush, h.heappop
a, A, P = [], [], {}
for _ in ' '*int(I()):
    p, l = map(int, I().split())
    i(a, (l, p)), i(A, (-l, -p))
    P[p] = l
for _ in ' '*int(I()):
    c, *x = I().split()
    x = (*map(int, x),)
    if c[0] == 'r':
        f = x[0] > 0
        H, v = (A, -1) if f else (a, 1)
        l, p = d(H)
        while H and P.get(p*v) != l*v:
            l, p = d(H)
        print(p*v)
        i(H, (l, p))
    elif c[0] == 'a':
        p, l = x
        i(a, (l, p))
        i(A, (-l, -p))
        P[p] = l
    else:
        P.pop(x[0])
