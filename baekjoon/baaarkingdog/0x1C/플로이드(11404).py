M = 2**27
I, R = input, range
n = int(I())
C = [[M]*n for _ in ' '*n]
for _ in ' '*int(I()):
    a, b, c = map(int, I().split())
    C[a-1][b-1] = min(C[a-1][b-1], c)
for k in R(n):
    C[k][k] = 0
    for i in R(n):
        for j in R(n):
            C[i][j] = min(C[i][j], C[i][k]+C[k][j])
for l in C:
    print(*(i % M for i in l))
