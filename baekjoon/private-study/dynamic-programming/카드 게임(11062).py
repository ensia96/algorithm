def f(x, y, z):
    if x <= y and not D[x][y]:
        Z = not z
        T, t = f(x+1, y, Z), f(x, y-1, Z)
        D[x][y] = [max(T+A[x], t+A[y]), min(T, t)][z]
    return D[x][y]


for _ in ' '*int(input()):
    n = int(input())
    A = [*map(int, input().split())]
    D = [[0]*-~n for _ in ' '*-~n]
    print(f(0, n-1, 0))
