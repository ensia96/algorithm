import sys
sys.setrecursionlimit(10**6)
I = sys.stdin.readline


def f(x):
    if G[x]-x:
        G[x] = f(G[x])
    return G[x]


g, p = int(I()), int(I())
G, P = [*range(g+1)], [int(I())for _ in ' '*p]
for i in range(p):
    y = f(P[i])
    if y == 0:
        i -= 1
        break
    G[y] = y-1
print(i+1)
