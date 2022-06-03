for _ in ' '*int(input()):
    n = int(input())
    A = [*map(int, input().split())]
    D = [[0]*n for _ in ' '*n]
    f = n % 2
    for s in range(n):
        for i in range(n-s):
            j, F = i+s, [min, max][f]
            D[i][j] = F(D[i+1][j]+A[i]*f, D[i][j-1]+A[j]*f)if s else A[i]*f
        f = not f
    print(D[0][-1])
