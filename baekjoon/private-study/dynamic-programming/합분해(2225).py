n, k = map(int, input().split())
D = [[1]*-~n]+[[0]*-~n for _ in ' '*~-k]
N = range(n+1)
for i in range(1, k):
    for j in N:
        D[i][j] = sum(D[i-1][j-k]for k in N if j >= k) % 1000000000
print(D[i][j])
