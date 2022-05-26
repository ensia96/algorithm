n, k = map(int, input().split())
D = [[0]*n for _ in ' '*n]
for i in range(n):
    D[i][i] = 1
    for j in range(i):
        D[i][j] = D[i-1][j]+D[i-1][j-1]
print(D[-1][k-1])
