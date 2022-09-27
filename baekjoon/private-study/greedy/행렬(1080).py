I, R = input, range
n, m = map(int, I().split())
A = [[*map(int, I())]for _ in ' '*n]
B = [[*map(int, I())]for _ in ' '*n]
c = 0


def f(i, j):
    for k in R(3):
        for l in R(3):
            A[i+k][j+l] = not A[i+k][j+l]
    return 1


def g(i):
    for j in R(m-2, m):
        if A[i][j] != B[i][j]:
            print(-1)
            return 1


for i in R(n-2):
    for j in R(m-2):
        c += A[i][j]-B[i][j] and f(i, j)
    if g(i):
        break
else:
    for i in R(n-2, n):
        if g(i):
            break
    else:
        print(c)
