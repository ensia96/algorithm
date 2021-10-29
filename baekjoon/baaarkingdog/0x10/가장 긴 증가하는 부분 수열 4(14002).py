I, R = input, range
n, A = int(I()), [*map(int, I().split())]
D, P = [1]*n, [0]*n
for i in R(n):
    for j in R(i):
        if A[j] < A[i]:
            D[i] = max(D[i], D[j]+1)
            if D[i] >= max(D):
                P[D[j]] = A[j]
a, P = D.index(max(D)), [*filter(None, P)]
print(D[a])
print(*P, A[a])
