n = int(input())
D = [[0]*-~n for _ in ' '*-~n]
A = [(0, 0)]+[(*map(int, input().split()),)for _ in ' '*n]
for i in range(1, n):
    for j in range(1, n-i+1):
        h = i+j
        D[j][h] = min(D[j][k]+D[k+1][h]+A[j][0]*A[k][1]*A[h][1]
                      for k in range(j, h))
print(D[1][n])
