I, R = input, range
n, A = int(I()), [*map(int, I().split())]
D, P = [1]*n, [0]*n
for i in R(n):
    for j in R(i):
        if A[j] < A[i]:
            D[i], P[D[j]] = max(D[i], D[j]+1), A[j]
a, P = D.index(max(D)), [*filter(None, P)]
print(D[a])
print(*P, A[a])
