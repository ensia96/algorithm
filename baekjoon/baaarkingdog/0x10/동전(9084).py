I, T, R = input, int, range
N, L = lambda: T(I()), lambda: [*map(T, I().split())]
for _ in R(N()):
    n, C, m = N(), [0]+L(), N()
    D = [[0]*(n+1) for _ in R(m+1)]
    for j in R(1, n+1):
        D[C[j]][j] = 1
        for i in R(1, m+1):
            D[i][j] += D[i][j-1]+D[i-C[j]][j]
    print(D[m][n])
