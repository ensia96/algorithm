M, N = 8**8, range(5)
D = [[M]*5 for _ in N]
D[0][0], f = 0, lambda x, y: not x and 2 or 3-(x == y)*2+(abs(x-y) == 2)
for a in map(int, input().split()):
    if not a:
        exit(print(min(map(min, D))))
    d = [[M]*5 for _ in N]
    for i in N:
        for j in N:
            d[a][j] = min(d[a][j], D[i][j]+f(i, a))
            d[i][a] = min(d[i][a], D[i][j]+f(j, a))
    D = d
