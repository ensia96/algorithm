I = input
for _ in range(int(I())):
    _, C, m = I(), map(int, I().split()), int(I())
    D = [1]+[0]*m
    for c in C:
        for i in range(c, m+1):
            D[i] += D[i-c]
    print(D[m])
