def f(x):
    if G[x]-x:
        G[x] = f(G[x])
    return G[x]


while 1:
    m, n = map(int, input().split())
    m or exit()
    G = [*range(n+1)]
    A = 0
    for x, y, z in sorted((*map(int, input().split()[::-1]),)for _ in ' '*n):
        y, z = f(y), f(z)
        if y-z:
            G[max(y, z)] = min(y, z)
        else:
            A += x
    print(A)
