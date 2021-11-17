l, r = lambda: map(int, input().split()), range
n, m = l()
b, N = [0]+[[*l()]for _ in r(n)], n+1
d = [[0]*N for _ in r(N)]
for i in r(1, N):
    for j in r(1, N):
        d[i][j] = d[i][j-1]+b[i][j-1]
for _ in r(m):
    h, i, j, k = l()
    print(sum(d[p][k]-d[p][i-1]for p in r(h, j+1)))
