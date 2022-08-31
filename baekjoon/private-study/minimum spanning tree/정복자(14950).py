n, m, t = map(int, input().split())
E = sorted((*map(int, input().split()[::-1]),)for _ in ' '*m)
G = [*range(n+1)]
A = sum(range(n-1))*t


def f(x):
    if G[x]-x:
        G[x] = f(G[x])
    return G[x]


for x, y, z in E:
    y, z = f(y), f(z)
    if y-z:
        G[max(y, z)] = min(y, z)
        A += x
print(A)
