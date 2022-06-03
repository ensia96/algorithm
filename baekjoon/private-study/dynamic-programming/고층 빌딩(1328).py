n, l, r = map(int, input().split())
D = [[[0]*n for _ in ' '*n]for _ in ' '*n]
D[0][0][0] = 1
for i in range(1, n):
    for j in range(n):
        for k in range(n):
            D[i][j][k] = (D[i-1][j-1][k]+D[i-1][j][k-1] +
                          D[i-1][j][k]*(i-1)) % 1000000007
print(D[n-1][l-1][r-1])
