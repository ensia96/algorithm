I, R = input, range
n, A = int(I()), [*map(int, I().split())]
D, P = [1]*n, [-1]*n
for i in R(n):
    for j in R(i):
        if A[j] < A[i]:
            C = D[j]+1
            D[i] = max(D[i], C)
            if (P[C] == -1)+((j < P[C])*(A[j] < A[C])):
                P[D[j]] = j
a = D.index(max(D))
print(D[a])
print(*[A[p]for p in P if p > -1], A[a])
