I, T, R = input, int, range
for _ in R(T(I())):
    _, C, m = I(), [*map(T, I().split())], T(I())
    D = [0]*(m+1)
    for c in C:
        for i in R(c, m+1):
            D[i] += (i == c)+D[i-c]
    print(D[m])
