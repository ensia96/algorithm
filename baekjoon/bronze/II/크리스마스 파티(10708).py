n, m, *A = map(int, open(0).read().split())
T, A = A[:m], A[m:]
S = [0] * n
for i in range(m):
    R = [T[i] == A[i * n + j] for j in range(n)]
    for j in range(n):
        S[j] += R[j] + (j == T[i] - 1) * (n - sum(R))
for s in S:
    print(s)
