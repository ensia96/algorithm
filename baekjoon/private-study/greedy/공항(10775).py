import sys
sys.setrecursionlimit(10**6)


def f(x):
    if G[x]-x:
        G[x] = f(G[x])
    return G[x]


g, p = int(input()), int(input())
G, P = [*range(g+1)], [int(input())for _ in ' '*p]
for i in range(p):
    y = f(P[i])
    if y == 0:
        i -= 1
        break
    G[y] = y-1
print(i+1)
