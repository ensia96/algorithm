n, m = map(int, input().split())
m = min(m, n-m)
D = [[0]*n for _ in ' '*n]
for i in range(n):
    D[i][i] = 1
for i in range(n):
    for j in range(n):
        D[i][j] = D[i-1][j]+D[i-1][j-1]
print(D[n-1][m-1])
