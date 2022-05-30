n, m = map(int, input().split())
B = [[*input()]for _ in ' '*n]
D = [[0]*m for _ in ' '*n]


def f(x, y, v):
    if D[x][y]:
        (v & 1 << (x*m+y)) and exit(print(-1))
        return D[x][y]
    D[x][y], v, t = 1, v | (1 << x*m+y), int(B[x][y])
    for i, j in [(x+t, y), (x-t, y), (x, y+t), (x, y-t)]:
        if (0 <= i < n)*(0 <= j < m) and B[i][j] != 'H':
            D[x][y] = max(D[x][y], f(i, j, v)+1)
    return D[x][y]


print(f(0, 0, 0))
