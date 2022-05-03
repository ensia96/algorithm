n, s, m = map(int, input().split())
V = [*map(int, input().split())]
D = [[0]*-~m for _ in ' '*-~n]
D[0][s] = 1
for i in range(n):
    for j in range(m+1):
        if D[i][j]:
            if j+V[i] <= m:
                D[i+1][j+V[i]] = 1
            if j-V[i] >= 0:
                D[i+1][j-V[i]] = 1
print(max([i for i in range(m+1)if D[n][i]]+[-1]))
