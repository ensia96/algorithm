I, R = input, range
n, A = int(I()), [*map(int, I().split())]
D, P = [0]*n, [0]*n
F, C, S = lambda x: [] if x == -1 else F(P[x]) + [A[x]], 0, 0
for i in R(n):
    D[i], P[i] = 1, -1
    for j in R(i):
        if (D[i] < D[j]+1)*(A[i] > A[j]):
            D[i], P[i] = D[j]+1, j
    if C < D[i]:
        C, S = D[i], i
print(C)
print(*F(S))
