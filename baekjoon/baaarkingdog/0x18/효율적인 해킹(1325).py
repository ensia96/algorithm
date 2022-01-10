l, A = lambda: map(int, input().split()), {}
n, m = l()
n += 1
C = [[]for _ in ' '*n]
for _ in ' '*m:
    a, b = l()
    C[b] += [a]
for i in range(1, n):
    q, v = [i], [0]*n
    v[i] = 1
    for c in q:
        for t in C[c]:
            if not v[t]:
                q += [t]
                v[t] = 1
    s = len(q)-1
    A[s] = A.get(s, [])+[i]
print(*A[max(A)])
