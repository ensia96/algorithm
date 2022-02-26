L, M = lambda: map(int, input().split()), 8**4
n, m, r = L()
I, N = [*L()], range(n)
C = [[M]*n for _ in ' '*n]
for _ in ' '*r:
    a, b, l = L()
    C[a-1][b-1] = C[b-1][a-1] = l
for k in N:
    for i in N:
        for j in N:
            C[i][j] = min(C[i][j], C[i][k]+C[k][j])
print(max(I[i]+sum(I[j]for j in N if(C[i][j] % M)*(C[i][j] <= m))for i in N))
