n = 60
D = [[0]*n for _ in ' '*n]
for i in range(n):
    D[i][i] = 1
for i in range(n):
    for j in range(n):
        D[i][j] = D[i-1][j]+D[i-1][j-1]
while n:
    n = int(input())
    n and print(D[2*n-1][n-1]-D[2*n-1][n-2])
