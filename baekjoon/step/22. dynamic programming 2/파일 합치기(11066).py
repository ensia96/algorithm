def f(x, y):
    if D[x][y]+(x == y):
        return D[x][y]
    D[x][y] = min(f(x, i)+f(i+1, y)for i in range(x, y))+F[y]-F[x-1]
    return D[x][y]


for _ in ' '*int(input()):
    k, t = int(input()), 0
    F = [*map(int, input().split())]+[0]
    D = [[0]*-~k for _ in ' '*-~k]
    for i in range(1, k):
        D[i-1][i] = F[i-1]+F[i]
    for i in range(1, k):
        F[i] += F[i-1]
    print(f(0, k-1))
