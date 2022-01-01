import sys
import heapq as h
I, l = sys.stdin.readline, lambda: map(int, input().split())
n, q = l()
u, o = h.heappush, h.heappop
d, A, D, H = 0, [*l()], {}, []
for i in range(n):
    if A[i]:
        D[i] = 1
        H += [i]
for _ in ' '*q:
    x, *y = l()
    if x == 1:
        i = y[0]-1
        f = D.get(i)
        D[i] = not f
        u(H, (i < d)*n+i)
    elif x == 2:
        d = (d+y[0]) % n
    else:
        while H:
            i = o(H)
            f, g = i < d, D[i % n]
            if not g:
                continue
            u(H, f*n+(i % n))
            if not f:
                print(i-d)
                break
        if not H:
            print(-1)
