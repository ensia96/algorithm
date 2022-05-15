n, m, r = int(input()), 8**8, range(3)
C = [[*map(int, input().split())]for _ in ' '*n]
A = m
for j in r:
    D = [m]*3
    D[j] = C[0][j]
    for i in range(1, n):
        D = min(D[1:])+C[i][0], min(D[0], D[2])+C[i][1], min(D[:2])+C[i][2]
    A = min([D[k]for k in r if j-k]+[A])
print(A)
