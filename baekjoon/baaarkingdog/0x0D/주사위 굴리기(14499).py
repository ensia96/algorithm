l, _ = lambda: map(int, input().split()), 0
n, m, x, y, k = l()
b, c, d = [[*l()] for _ in range(n)], [*l()], [0]*6

for t in c:
    t -= 1
    i, j = [(x, y+1), (x, y-1), (x-1, y), (x+1, y)][t]
    if 0 <= i < n and 0 <= j < m:
        d = [d[[3, 2, 5, 4][t]], d[[2, 3, 4, 5][t]], d[[0, 1, 2, 2][t]],
             d[[1, 0, 3, 3][t]], d[[4, 4, 0, 1][t]], d[[5, 5, 1, 0][t]]]
        x, y = i, j
        if b[x][y]:
            d[1] = b[x][y]
            b[x][y] = 0
        else:
            b[x][y] = d[1]
        print(d[0])
