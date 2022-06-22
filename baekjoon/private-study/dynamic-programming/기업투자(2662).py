n, m = map(int, input().split())
A = [[*map(int, input().split())]for _ in ' '*n]
D, P, R = -~n*[0], [-~n*[0]for _ in ' '*m], []
for i in range(m):
    for j in range(n, 0, -1):
        for k in range(j):
            if D[j] < D[j-k-1]+A[k][i+1]:
                D[j], P[i][j] = D[j-k-1]+A[k][i+1], k+1
while m:
    m -= 1
    R += P[m][n],
    n -= P[m][n]
print(D[-1])
print(*R[::-1])
