n = int(input())
g = [[*map(int, input().split())]for _ in ' '*n]
for k in range(n):
    for i in range(n):
        for j in range(n):
            g[i][j] = g[i][j] or g[i][k]*g[k][j]
for l in g:
    print(*l)
