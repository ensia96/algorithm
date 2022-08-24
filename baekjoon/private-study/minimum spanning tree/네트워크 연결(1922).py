n = int(input())
A, G = 0, [*range(n+1)]


def f(x):
    if G[x]-x:
        G[x] = f(G[x])
    return G[x]


for x, y, z in sorted((*map(int, input().split()[::-1]),)for _ in ' '*int(input())):
    y, z = f(y), f(z)
    if y-z:
        G[max(y, z)] = min(y, z)
        A += x
print(A)
