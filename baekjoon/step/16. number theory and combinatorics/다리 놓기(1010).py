D = [[1]*31]+[[0]*31 for _ in ' '*30]
for i in range(1, 31):
    for j in range(i, 31):
        D[i][j] = D[i-1][j-1]+D[i][j-1]
for _ in ' '*int(input()):
    n, m = map(int, input().split())
    print(D[n][m])
