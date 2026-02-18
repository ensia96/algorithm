n, m, *A = map(int, open(0).read().split())
M = [i := 0] * m
while n * sum(A):
    t = A[i] > 0
    M[i] += t
    A[i] -= t
    n -= t
    i = -~i % m
print(*M)
