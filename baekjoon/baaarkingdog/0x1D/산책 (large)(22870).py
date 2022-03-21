import sys
import heapq as h
L, M = lambda: map(int, sys.stdin.readline().split()), 9**9
n, m = L()
n += 1
E, N = [[]for _ in ' '*n], [1]*n
for _ in ' '*m:
    a, b, c = L()
    E[a] += (b, c),
    E[b] += (a, c),
for e in E:
    e.sort()
s, e = L()


def F():
    D, Q = [M]*n, [(0, s)]
    D[s] = 0
    while Q:
        x, y = h.heappop(Q)
        if D[y]-x:
            continue
        for i, j in E[y]:
            if D[i] > D[y]+j and N[i]:
                D[i] = D[y]+j
                h.heappush(Q, (D[i], i))
    return D[e]


def D(x, y):
    if x == e or y > A:
        return y == A
    for i, j in E[x]:
        if N[i]:
            N[i] = 0
            if D(i, y+j):
                return 1
            N[i] = 1


A = F()
D(s, 0)
N[e] = 1
print(A+F())
