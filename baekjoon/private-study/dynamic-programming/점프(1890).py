n = int(input())
A = [[*map(int, input().split())]for _ in ' '*n]
D = [[0]*n for _ in ' '*n]
D[0][0] = 1
for i in range(n):
    for j in range(n):
        t = A[i][j]
        if D[i][j]*((i, j) != (n-1, n-1)):
            if j+t < n:
                D[i][j+t] += D[i][j]
            if i+t < n:
                D[i+t][j] += D[i][j]
print(D[n-1][n-1])
