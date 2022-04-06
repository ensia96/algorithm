I, R = input, range


def f(x, y):
    if not D[x][y]+(x == y):
        D[x][y] = min(f(x, i)+f(i+1, y)for i in R(x, y))+F[y]-F[x-1]
    return D[x][y]


for _ in ' '*int(I()):
    k = int(I())
    F = [*map(int, I().split())]+[0]
    D = [[0]*k for _ in ' '*k]
    for i in R(1, k):
        D[i-1][i] = F[i-1]+F[i]
    for i in R(1, k):
        F[i] += F[i-1]
    print(f(0, k-1))
