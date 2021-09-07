R = range
n, m = map(int, input().split())
D = [[*map(int, input())]for _ in R(n)]
for i in R(1, n):
    for j in R(1, m):
        D[i][j] += min(D[i-1][j-1], D[i-1][j], D[i][j-1])*D[i][j]
print(max(map(max, D))**2)
