l, A = lambda: map(int, input().split()), {}
n, m = l()
n += 1
F = [[]for _ in ' '*n]
for _ in ' '*m:
    a, b = l()
    F[a], F[b] = F[a]+[b], F[b]+[a]
for i in range(1, n):
    q, v, s = [(i, 0)], [0]*n, 0
    v[i] = 1
    for p, d in q:
        for f in F[p]:
            if not v[f]:
                q += [(f, d+1)]
                s, v[f] = s+d+1, 1
    A[s] = A.get(s) or i
print(A[min(A)])
