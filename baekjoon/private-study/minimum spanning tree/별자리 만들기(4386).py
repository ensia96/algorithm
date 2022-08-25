n = int(input())
r = range
A = [(*map(float, input().split()),)for _ in ' '*n]
G = [*r(n)]
D = 0


def f(x):
    if G[x]-x:
        G[x] = f(G[x])
    return G[x]


Q = []
for x, y, z in sorted((((A[i][0]-A[j][0])**2+(A[i][1]-A[j][1])**2)**.5, i, j)for i in r(n)for j in r(i+1, n)):
    y, z = f(y), f(z)
    if y-z:
        G[max(y, z)] = min(y, z)
        D += x

print(f"{D:.2f}")
