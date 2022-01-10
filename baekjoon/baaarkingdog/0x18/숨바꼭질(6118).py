l, A = lambda: map(int, input().split()), {}
n, m = l()
n += 1
C = [[]for _ in ' '*n]
for _ in ' '*m:
    a, b = l()
    C[a], C[b] = C[a]+[b], C[b]+[a]
q, v = [(1, 0)], [0]*n
v[1] = 1
for b, d in q:
    for c in C[b]:
        if not v[c]:
            q += [(c, d+1)]
            v[c], A[d+1] = 1, A.get(d+1, [])+[c]
d = max(A)
print(min(A[d]), d, len(A[d]))
