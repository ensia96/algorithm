l, Q = lambda: map(int, input().split()), [(0, 0)]
n, m = l()
A = [[*l()]+[0]for _ in ' '*n]
D = [[0]*-~m for _ in ' '*n]
for i in range(n):
    for j in range(m):
        D[i][j] = max(D[i-1][j], D[i][j-1], D[i-1][j-1])+A[i][j]
print(D[n-1][m-1])
