n, m = int(input()), 8**8
C = [[*map(int, input().split())]for _ in ' '*n]


def f(j):
    D = [m]*3
    D[j] = C[0][j]
    x, y, z = D
    for i in range(1, n):
        a, b, c = C[i]
        x, y, z = min(y, z)+a, min(x, z)+b, min(x, y)+c
    return min([x, y, z][k]for k in range(3)if j-k)


print(min(f(0), f(1), f(2)))
