import sys
import heapq as h
from collections import defaultdict
I, i, d = sys.stdin.readline, h.heappush, h.heappop
G, L, P = {}, {}, {}


class X():
    def __init__(self, p): self.p, self.h, self.H = p, [], []
    def P(self, p, l): i(self.h, (l, p)); i(self.H, (-l, -p))

    def F(self, f):
        T, f = self.H if f > 0 else self.h, 1+(f > 0)*-2
        while T and P.get(f*T[0][1]) != (self.p, f*T[0][0]):
            d(T)
        if T:
            return f*T[0][0], f*T[0][1]


class Y():
    def __init__(self, p): self.p, self.h, self.H = p, [], []
    def P(self, p): i(self.h, p); i(self.H, -p)

    def F(self, x):
        T = self.h if x > 0 else self.H
        while T and P.get(x*T[0], (0, -1))[1] != self.p:
            d(T)
        if T:
            return x*T[0]


def A(p, l, g):
    G[g] = G.get(g, X(g))
    G[g].P(p, l)
    L[l] = L.get(l, Y(l))
    L[l].P(p)
    P[p] = (g, l)


for _ in ' '*int(I()):
    A(*map(int, I().split()))
for _ in ' '*int(I()):
    c, *a = I().split()
    if c[0] == 'a':
        A(*map(int, a))
    elif c[0] == 's':
        P.pop(int(a[0]))
    elif c[-1] == 'd':
        g, x = map(int, a)
        print(G[g].F(x)[1])
    elif c[-1] == '2':
        x = int(a[0])
        s, r = 0 if x == 1 else 100001, -1
        for g in G:
            R = G[g].F(x)
            if not R:
                continue
            if x > 0:
                if R[0] > s:
                    s, r = R
                elif R[0] == s:
                    r = max(r, R[1])
            else:
                if R[0] < s:
                    s, r = R
                elif R[0] == s:
                    r = min(r, R[1])
        print(r)
    else:
        f, l = map(int, a)
        l, r = l+f*(f < 0), -1
        while r < 0 and 0 <= l <= 100:
            r = L[l].F(f) if L.get(l) else -1
            l += f
        print(r)
