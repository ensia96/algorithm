A = input()
B = [input(), input()]
a = len(A)
b = len(B[0])
D = [[a*[-1]for _ in ' '*b]for _ in '  ']


def f(x, y, z):
    if y == b:
        return z == a
    elif z == a:
        return 1
    elif D[x][y][z] == -1:
        D[x][y][z] = 0
        for i in range(y, b):
            if B[not x][i] == A[z]:
                D[x][y][z] += f(not x, i+1, z+1)
    return D[x][y][z]


print(f(0, 0, 0)+f(1, 0, 0))
