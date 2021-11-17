import sys
l, r = lambda: map(int, sys.stdin.readline().split()), range
n, m = l()
N = n+1
b = [[*l()]for _ in r(n)]
d = [[0]*N for _ in r(N)]
for i in r(n):
    for j in r(n):
        d[i+1][j+1] = d[i+1][j]+d[i][j+1]-d[i][j]+b[i][j]
for _ in r(m):
    h, i, j, k = l()
    print(d[j][k]+d[h-1][i-1]-d[h-1][k]-d[j][i-1])
