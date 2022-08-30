n, m = map(int, input().split())
s, e = map(int, input().split())
E = []
G = [*range(n+1)]
for _ in ' '*m:
    h1, h2, k = map(int, input().split())
    E += (-k, h1, h2),


def f(x):
    if G[x]-x:
        G[x] = f(G[x])
    return G[x]


for x, y, z in sorted(E):
    y, z = f(y), f(z)
    if y-z:
        G[max(y, z)] = min(y, z)
        f(s)-f(e) or exit(print(-x))
print(0)
