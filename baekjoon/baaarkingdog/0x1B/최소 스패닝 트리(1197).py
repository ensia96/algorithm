I, *L = open(0)
v, e = map(int, I.split())
A = C = 0
G = [-1]*-~v


def F(x):
    if G[x] < 0:
        return x
    G[x] = F(G[x])
    return G[x]


def D(u, v):
    u, v = F(u), F(v)
    if u == v:
        return 0
    if G[u] == G[v]:
        G[u] -= 1
    if G[u] < G[v]:
        G[v] = u
    else:
        G[u] = v
    return 1


for c, a, b in sorted((*map(int, l.split()[::-1]),)for l in L):
    if D(a, b):
        continue
    A += c
    C += 1
    if not C+1-v:
        break
print(A)
