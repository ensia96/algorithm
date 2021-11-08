I, T, R = input, int, range
N, L = lambda: T(I()), lambda: [*map(T, I().split())]
for _ in R(N()):
    n, C, m = N(), [0]+L(), N()
    D = [0]*(m+1)
    for c in C:
        if c > m:
            break
        for i in R(1, m+1):
            D[i] += (i == c)+D[i-c]*(i > c)
    print(D[m])
