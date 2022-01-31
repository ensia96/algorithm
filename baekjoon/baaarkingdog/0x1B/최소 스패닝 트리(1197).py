I, *L = open(0)
v, e = map(int, I.split())
A = C = 0
G = [*range(v+1)]


def F(x):
    if G[x] != x:
        G[x] = F(G[x])
    return G[x]


for c, a, b in sorted((*map(int, l.split()[::-1]),)for l in L):
    a, b = F(a), F(b)
    if F(a) != F(b):
        G[max(a, b)] = min(a, b)
        A += c
print(A)
