l, r = lambda: map(int, input().split()), range
n, m = l()
N = n+1
b = [[0]*N]+[[0, *l()]for _ in r(n)]
d = [[0]*N for _ in r(N)]
for i in r(1, N):
    for j in r(1, N):
        d[i][j] = d[i][j-1]+d[i-1][j]-d[i-1][j-1]+b[i][j]
for _ in r(m):
    h, i, j, k = l()
    print(d[j][k]+d[h-1][i-1]-d[h-1][k]-d[j][i-1])
