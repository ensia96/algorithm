for _ in ' '*int(input()):
    n, X, D = int(input()), [*map(int, input().split())], [0]
    for i in range(n):
        D += D[-1]+X[i],
    print(max(D[i+1]-D[j]for i in range(n)for j in range(i+1)))
