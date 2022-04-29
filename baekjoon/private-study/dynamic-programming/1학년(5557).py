n = int(input())
A = [*map(int, input().split())]
D = [[0]*21 for _ in ' '*n]
D[0][A[0]] = 1
for i in range(1, n):
    for j in range(21):
        if j-A[i] >= 0:
            D[i][j-A[i]] += D[i-1][j]
        if j+A[i] <= 20:
            D[i][j+A[i]] += D[i-1][j]
print(D[n-2][A[n-1]])
