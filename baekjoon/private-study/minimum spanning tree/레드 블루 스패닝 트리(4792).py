def F(x):
    if G[x]-x:
        G[x] = F(G[x])
    return G[x]


while 1:
    n, m, k = map(int, input().split())
    n or exit()
    R, B = [], []
    for _ in ' '*m:
        c, f, t = input().split()
        f, t = int(f), int(t)
        R += (c == 'B', f, t),
        B += (c == 'R', f, t),
    m, G = 0, [*range(n+1)]
    for x, y, z in sorted(R):
        y, z = F(y), F(z)
        if y-z:
            G[max(y, z)] = min(y, z)
            m += x
    M, G = n-1, [*range(n+1)]
    for x, y, z in sorted(B):
        y, z = F(y), F(z)
        if y-z:
            G[max(y, z)] = min(y, z)
            M -= x
    print(+(m <= k <= M))
