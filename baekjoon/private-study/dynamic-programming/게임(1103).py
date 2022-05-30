n, m = map(int, input().split())
B = [[*input()]for _ in ' '*n]
D, V = [[0]*m for _ in ' '*n], [[0]*m for _ in ' '*n]
V[0][0] = 1


def f(x, y):
    if D[x][y]:
        V[x][y] and exit(print(-1))
        return D[x][y]
    D[x][y] = V[x][y] = 1
    t = int(B[x][y])
    for i, j in [(x+t, y), (x-t, y), (x, y+t), (x, y-t)]:
        if (0 <= i < n)*(0 <= j < m) and B[i][j] != 'H':
            D[x][y] = max(D[x][y], f(i, j)+1)
    V[x][y] = 0
    return D[x][y]


print(f(0, 0))
