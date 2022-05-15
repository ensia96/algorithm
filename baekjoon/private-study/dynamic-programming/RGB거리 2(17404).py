n, m = int(input()), 8**8
C = [[*map(int, input().split())]for _ in ' '*n]
A = m
for j in range(3):
    D = [m*(i != j)+C[0][i] for i in range(3)]
    for i in range(1, n):
        D = min(D[1:])+C[i][0], min(D[0], D[2])+C[i][1], min(D[:2])+C[i][2]
    A = min([D[k]for k in range(3)if j-k]+[A])
print(A)
