l, r = lambda: map(int, input().split()), range
n, m = l()
A = [*l()]
C = [*l()]
k = sum(C)+1
D = [[0]*k for _ in ' '*n]
for i in r(n):
    for j in r(k):
        D[i][j] = max(D[i-1][j], (D[i-1][j-C[i]]+A[i])*(j-C[i] >= 0))
for j in r(k):
    if D[n-1][j] >= m:
        exit(print(j))
