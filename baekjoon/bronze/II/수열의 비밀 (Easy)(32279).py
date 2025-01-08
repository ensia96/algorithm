n, p, q, r, s, *A = map(int, open(0).read().split())
for i in range(n - 1):
    A += ([p * A[i // 2] + q, r * A[i // 2] + s][i % 2],)
print(sum(A))
