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


T = [[]for _ in ' '*-~n]
for x, y, z in sorted(E):
    y, z = f(y), f(z)
    if y-z:
        G[max(y, z)] = min(y, z)
        T[y] += (z, -x),
        T[z] += (y, -x),
Q, A, V, C = [s], 0, [1]*-~n, [0]*-~n
V[s] = 0
while Q:
    q = []
    for c in Q:
        for x, y in T[c]:
            if V[x]:
                V[x], C[x] = 0, C[c]+y
                q += x,
    Q = q
print(C[e])
