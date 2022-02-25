M = 2**17
I, R = input, range
n = int(I())
m = int(I())
C = [[M]*n for _ in ' '*n]
for _ in ' '*m:
    a, b, c = map(int, I().split())
    C[a-1][b-1] = min(C[a-1][b-1], c)
for i in R(n):
    C[i][i] = 0
for k in R(n):
    for i in R(n):
        for j in R(n):
            C[i][j] = min(C[i][j], C[i][k]+C[k][j])
for l in [[0 if C[i][j] == M else C[i][j]for j in R(n)]for i in R(n)]:
    print(*l)
