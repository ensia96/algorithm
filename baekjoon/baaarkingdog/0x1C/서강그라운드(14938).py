L, M, A = lambda: map(int, input().split()), 8**4, 0
n, m, r = L()
I, N = [*L()], range(n)
C = [[M]*n for _ in ' '*n]
R = [[0]*n for _ in ' '*n]
for _ in ' '*r:
    a, b, l = L()
    a, b = a-1, b-1
    C[a][b] = C[b][a] = l
    R[a][b], R[b][a] = b, a
for k in N:
    for i in N:
        for j in N:
            t = C[i][k]+C[k][j]
            if C[i][j] > t:
                C[i][j], R[i][j] = t, R[i][k]
for i in N:
    V = {i}
    for j in N:
        if not C[i][j] % M or C[i][j] > m:
            continue
        r = [i]
        while r[-1] != j:
            r += R[r[-1]][j],
        V = {*V, *r}
    A = max(A, sum(I[c]for c in V))
print(A)
