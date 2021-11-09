I, R = input, range
n, m = map(int, I().split())
D = [[*map(int, I())]for _ in R(n)]
for i in R(1, n):
    for j in R(1, m):
        if D[i][j]:
            t = [D[i-1][j-1], D[i-1][j], D[i][j-1]]
            D[i][j] += min(t)*all(t)
print(max(map(max, D))**2)
