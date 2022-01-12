n, *I = open(0)
n = int(n)
F, D = [[] for _ in ' '*(n+1)], {}
for l in I[:-1]:
    a, b = map(int, l.split())
    F[a], F[b] = F[a]+[b], F[b]+[a]
for i in range(n):
    q, v, m = [(i+1, 0)], [0]*(n+1), 0
    v[i] = 1
    for p, d in q:
        for f in F[p]:
            if not v[f]:
                q += [(f, d+1)]
                m, v[f] = max(m, d+1), 1
    D[m] = D.get(m, [])+[i+1]
A = D[min(D)]
print(min(D), len(A))
print(*A)
