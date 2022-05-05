n, m, k = map(int, input().split())
D = [[0]*m for _ in ' '*n]
D[0][0] = 1
for i in range(n):
    for j in range(m):
        if i+j:
            D[i][j] = D[i-1][j]+D[i][j-1]
x, y = divmod(k-1, m)if k else(0, 0)
print(D[x][y]*D[n-1-x][m-1-y])
