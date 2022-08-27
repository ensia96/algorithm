n, m = map(int, input().split())
A = [0]+input().split()
G = [*range(n+1)]
E = C = 0


def f(x):
    if G[x]-x:
        G[x] = f(G[x])
    return G[x]


for x, y, z in sorted((*map(int, input().split()[::-1]),)for _ in ' '*m):
    if A[y] == A[z]:
        continue
    y, z = f(y), f(z)
    if y-z:
        G[max(y, z)] = min(y, z)
        E += x
        C += 1
print(C-n+1 and -1 or E)
