n = int(input())
A = [[*map(int, input().split())]for _ in ' '*n]
D = [[3*[-1]for _ in ' '*n]for _ in ' '*n]


def f(x, y, z):
    if (x, y) == (n-1, n-1):
        D[x][y][z] = 1
    elif D[x][y][z] == -1:
        D[x][y][z], t = 0, ((x, y+1), (x+1, y+1), (x+1, y))
        for i in ((0, 1), (0, 1, 2), (1, 2))[z]:
            if all((i < n)*(j < n) and not A[i][j]for i, j in (t[:1], t, t[2:])[i]):
                D[x][y][z] += f(*t[i], i)
    return D[x][y][z]


print(f(0, 1, 0))
