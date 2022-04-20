l, Q = lambda: map(int, input().split()), [(0, 0)]
n, m = l()
A = [[*l()]for _ in ' '*n]
D = [[0]*m for _ in ' '*n]
D[0][0] = A[0][0]
for i, j in Q:
    for x, y in [(i+1, j), (i, j+1), (i+1, j+1)]:
        if (0 <= x < n)*(0 <= y < m) and D[i][j]+A[x][y] > D[x][y]:
            D[x][y] = D[i][j]+A[x][y]
            Q += (x, y),
print(D[n-1][m-1])
