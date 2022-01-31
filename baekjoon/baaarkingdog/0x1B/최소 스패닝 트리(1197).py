I, *L = open(0)
v, e = map(int, I.split())
A = C = 0
G = [*range(v+1)]


def F(x):
    if G[x] == x:
        return x
    G[x] = F(G[x])
    return G[x]


def D(u, v):
    u, v = F(u), F(v)
    if u < v:
        G[v] = u
    else:
        G[u] = v


for c, a, b in sorted((*map(int, l.split()[::-1]),)for l in L):
    if F(a) != F(b):
        D(a, b)
        A += c
print(A)
