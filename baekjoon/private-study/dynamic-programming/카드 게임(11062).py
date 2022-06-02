def f(x, y, z):
    if x <= y and not sum(D[x][y]):
        Z = not z
        T, t = f(x+1, y, Z), f(x, y-1, Z)
        i, j = [(t, y), (T, x)][T[z]+A[x] > t[z]+A[y]]
        a, b = i
        D[x][y] = (a+A[j]*Z, b+A[j]*z)
    return D[x][y]


for _ in ' '*int(input()):
    n = int(input())
    A = [*map(int, input().split())]
    D = [[(0, 0)]*-~n for _ in ' '*-~n]
    print(f(0, n-1, 0)[0])
